# -*- coding: utf-8 -*-
from ckiptagger import WS,construct_dictionary
import re

ws = WS("./data")

path = "C:/Users/ken99/PycharmProjects/hyphenation/Grammer_v6.txt"
with open(path, 'r', encoding='utf-8-sig') as f:
    key_word = f.read()
    # 將list轉成dict型態，這邊每個權重都設為1
    key_word=key_word.split('\n')
dict_for_CKIP = dict((el,1) for el in key_word)
dict_for_CKIP = construct_dictionary(dict_for_CKIP)

# 讀取文本（corpus）
cut_corpus = []
path = 'C:/Users/ken99/Desktop/hyphenation/txt/【文法基礎篇】Be Verb｜Be動詞的用法秘笈｜15分鐘精華解析｜Boro English.txt'
with open(path, 'r', encoding='utf-8') as f :
    corpus = f.readlines()

collect_corpus = []
for i in corpus:
    clean_c = re.sub(r'\n', '', i)
    if len(clean_c) > 0:
        collect_corpus.append(clean_c)


word_segment = ws(collect_corpus,
                  recommend_dictionary=dict_for_CKIP)
for i in word_segment:
    for word in i:
        cut_corpus.append(word)

print(cut_corpus)
