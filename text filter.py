import pandas as pd
import os

all_filtered_word = []
path = r'wordbook.txt'
with open(path, 'r', encoding='utf-8-sig') as f:
    key_word = f.read()
    key_word = key_word.split('\n')
    f.close()

path = r'median_tfidf.txt'
with open(path, 'r', encoding='utf-8-sig') as f:
    mid_tfidf = f.read()
    f.close()


for info in os.listdir(r'TF-IDF'):
    domain = os.path.abspath(r'TF-IDF')
    path = os.path.join(domain, info)
    filename = os.path.splitext(info)[0]
    fin_filtered = []
    with open(path, 'r', encoding='utf-8-sig'):
        usecols = ['word', 'TF-IDF']
        df = pd.read_csv(f'TF-IDF/{filename}.csv', usecols=usecols)
        final_df = df.sort_values(by=['TF-IDF'], ascending=False)
        final_df = final_df.head(50)
        dict_df = final_df.set_index('word').T.to_dict('list')
        all_tfidf_compare = []
        for x in dict_df:
            if dict_df[x][0] >= float(mid_tfidf):
                all_tfidf_compare.append(x)
        for word in all_tfidf_compare:
            if word in key_word:
                fin_filtered.append(word)
                if word in all_filtered_word:
                    continue
                all_filtered_word.append(word)

        path = f'fintxt/{filename}.txt'
        with open(path, 'w', encoding='utf-8-sig') as f:
            for i in fin_filtered:
                f.writelines(i + "\n")
        f.close()

path = f'filtered_all_keywords.txt'
with open(path, 'w', encoding='utf-8-sig') as f:
    for i in all_filtered_word:
        f.writelines(i + "\n")


