import math
import os
import pandas as pd
occurrences_of_word = {}

for info in os.listdir('./hyphenated_txt'):
    domain = os.path.abspath('./hyphenated_txt')
    path = os.path.join(domain, info)
    with open(path, 'r', encoding='utf-8-sig') as f:
        file = f.read().split('\n')
        del file[-1]   # 這次讀檔會多讀一個值所以把它刪掉，之後沒問題這行要拿掉
        words_count = []
        count = {}
        for word in file:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        words_count.append(count)
        all_words = []
        for word in words_count:
            all_words.extend(list(word.keys()))
        for word in all_words:
            if word in occurrences_of_word:
                occurrences_of_word[word] += 1
            else:
                occurrences_of_word[word] = 1

if not os.path.isdir('./TF-IDF'):
    os.mkdir('./TF-IDF')

all_tfidf = []
for info in os.listdir('./hyphenated_txt'):
    domain = os.path.abspath('./hyphenated_txt')
    path = os.path.join(domain, info)
    filename = os.path.splitext(info)[0]
    with open(path, 'r', encoding='utf-8-sig') as f:
        # 計算TF
        file = f.read()
        file = file.split('\n')
        del file[-1]    # 這次讀檔會多讀一個值所以把它刪掉，之後沒問題這行要拿掉
        words_count = []
        count = {}
        for word in file:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        words_count.append(count)
        count_all_word = len(file)
        tf = []
        for word in count:
            count[word] = round(count[word] / count_all_word, 5)
            tf.append(count[word])

        idf = []
        total_file = 0
        for path in os.listdir(r'hyphenated_txt'):
            if os.path.isfile(os.path.join(r'hyphenated_txt', path)):
                total_file += 1
        for word_count in words_count:
            inv_fre = {}
            for word in word_count.keys():
                occurrence = occurrences_of_word[word]
                inv_fre[word] = math.log(10, round((total_file/occurrence), 5))
                idf.append(inv_fre[word])

        tf_idf = [round(x*y, 5) for x, y in zip(tf, idf)]
        csv_dict = {'word': word_count.keys(), 'TF': tf, 'IDF': idf, 'TF-IDF': tf_idf}
        df = pd.DataFrame(csv_dict)
        df.to_csv(f'./TF-IDF/{filename}.csv', encoding='utf-8-sig', index=False)
        for x in tf_idf:
            all_tfidf.append(x)

all_tfidf.sort(reverse=True, key=float)
path = r'median_tfidf.txt'
with open(path, 'w', encoding='utf-8-sig') as f:
    f.write(str(all_tfidf[int((len(all_tfidf)/2))]))