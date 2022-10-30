from ast import keyword
import os
import pandas as pd

for info in os.listdir(f'C:/Users/ken/Desktop/text'):
    domain = os.path.abspath(f'C:/Users/ken/Desktop/text')
    path = os.path.join(domain, info)
    filename = os.path.splitext(info)[0]    
    with open(path, 'r', encoding='utf-8-sig')as f:
        file = f.read()
        file = file.split('\n')
        keywords = ''
        for x in file:
            keywords+= x+' '                             
        csv_dict = {'viedo_title':filename, 'keywords':[keywords]}
        df = pd.DataFrame(csv_dict)
        df.to_csv(f'C:/Users/ken/Desktop/all_csv.csv', mode='a', encoding='utf-8-sig', index=False, header=None)



