# -*- coding: utf-8 -*-
from ckiptagger import WS, construct_dictionary
import re, csv, os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

ws = WS("./data")

path = "C:/Users/ken99/PycharmProjects/hyphenation/Grammer_v6.txt"
with open(path, 'r', encoding='utf-8-sig') as f:
    key_word = f.read()
    # 將list轉成dict型態，這邊每個權重都設為1
    key_word = key_word.split('\n')
dict_for_CKIP = dict((el, 1) for el in key_word)
dict_for_CKIP = construct_dictionary(dict_for_CKIP)
f.close()

# 讀取文本（corpus）
for info in os.listdir('./txt'):
    domain = os.path.abspath('./txt') #獲取資料夾的路徑，此處其實沒必要這麼寫，目的是為了熟悉os的資料夾操作
    path = os.path.join(domain, info) #將路徑與檔名結合起來就是每個檔案的完整路徑
    filename = os.path.splitext(info)[0]
    with open(path, 'r', encoding='utf-8') as f:
        corpus = f.readlines()
    f.close()
    collect_corpus = []
    for i in corpus:
        clean_c = re.sub(r'\n', '', i)
        if len(clean_c) > 0:
            collect_corpus.append(clean_c)
    word_segment = ws(collect_corpus,
                      recommend_dictionary=dict_for_CKIP)
    cut_corpus = []
    for i in word_segment:
        for word in i:
            cut_corpus.append(word)
    if not os.path.isdir('./hyphenated_txt'):
        os.mkdir('./hyphenated_txt')
    df = pd.DataFrame(cut_corpus)
    df.to_csv(f'./hyphenated_txt/{filename}.csv', encoding='utf-8-sig')

path = 'C:/Users/ken99/PycharmProjects/hyphenation/stopWords_v11_3_3.txt'
with open(path, 'r', encoding='utf-8-sig') as f:
    stop_word = f.read()
    stop_word = stop_word.split('\n')
f.close()





text_cv = CountVectorizer(max_df=0.8, min_df=4, stop_words=stop_word)
td_matrix = text_cv.fit_transform(cut_corpus)
print(text_cv.vocabulary_.items())
# tfidf = TfidfTransformer()
# tfidf_matrix = tfidf.fit_transform(td_matrix)
# import pandas as pd
# df = pd.DataFrame(tfidf_matrix.T.toarray(), index=text_cv.vocabulary_.keys())
# df.to_csv('output.csv', index=text_cv.vocabulary_.keys(), encoding='utf-8-sig')
# with open('output.csv', 'w', newline='') as csvfile:
#   # 建立 CSV 檔寫入器
#   writer = csv.writer(csvfile)
#   writer.write(df)
#print(df)

# print(cut_corpus)
