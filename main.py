# -*- coding: utf-8 -*-
from ckiptagger import WS, construct_dictionary
import re
import os
import string
import nltk

nltk.download('punkt')
ws = WS("./data")

# 設定保留詞
path = "./savewords.txt"
with open(path, 'r', encoding='utf-8-sig') as f:
    key_word = f.read()
    # 將list轉成dict型態，這邊每個權重都設為1
    key_word = key_word.split('\n')
dict_for_CKIP = dict((el, 1) for el in key_word)
dict_for_CKIP = construct_dictionary(dict_for_CKIP)
f.close()

# 讀取文本（corpus）
for info in os.listdir('./txt'):
    domain = os.path.abspath('./txt')
    path = os.path.join(domain, info)
    filename = os.path.splitext(info)[0]
    with open(path, 'r', encoding='utf-8') as f:
        corpus = f.readlines()
    f.close()
    collect_corpus = []
    for i in corpus:
        clean_c = re.sub(r'\n', "", i)
        if len(clean_c) > 0:
            collect_corpus.append(clean_c)

    # 中文斷詞
    word_segment = ws(collect_corpus, recommend_dictionary=dict_for_CKIP)
    CHI_cut_corpus = []
    ENG_cut_corpus = []
    CHI_judge = re.compile(u'[\u4e00-\u9fa5]+')
    for i in word_segment:
        for word in i:
            if word in string.punctuation:
                continue
            match = CHI_judge.search(word)
            if match:
                CHI_cut_corpus.append(word)
            else:
                ENG_cut_corpus.append(word)
    fin_ENG = []
    # 英文斷詞
    for i in ENG_cut_corpus:
        sentences = nltk.word_tokenize(i)
        for eng_word in sentences:
            fin_ENG.append(eng_word)

    if not os.path.isdir('./hyphenated_txt'):
        os.mkdir('./hyphenated_txt')

    # 全部小寫
    lower_cut_corpus = []
    for i in fin_ENG:
        lower = i.lower()
        lower_cut_corpus.append(lower)
    all_words = CHI_cut_corpus+lower_cut_corpus

    # 刪除停用詞
    with open('./stopWords.txt', encoding='utf-8-sig') as f:
        stop_word = f.read()
        stop_words = stop_word.split('\n')
    fin_words = []
    for word in all_words:
        if word in stop_words:
            pass
        else:
            fin_words.append(word)

    path = f'./hyphenated_txt/{filename}.txt'
    with open(path, 'w', encoding='utf-8-sig') as f:
        for i in fin_words:
            f.writelines(i+"\n")
