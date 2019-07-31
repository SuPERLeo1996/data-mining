import csv
import pandas as pd

# with open('test-douban.csv',encoding='utf8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row[len(row)-1])

df = pd.read_csv('test-douban.csv')
# 显示所有列
df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
df['h'].to_csv('data.txt', header=None,index=None)
