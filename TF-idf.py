import os

for info in os.listdir('./hyphenated_txt'):
    domain = os.path.abspath('./hyphenated_txt')
    path = os.path.join(domain, info)
    filename = os.path.splitext(info)[0]
    with open(path, 'r', encoding='utf-8-sig') as f:
        file = f.read()
        file = file.split('\n')
        fre_words_count = []
        count = {}
        for word in file:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
        count_all_word = len(file)
        for word in count:
            count[word] = round(count[word]/count_all_word, 5)
        fre_words_count.append(count)
    print(fre_words_count)
