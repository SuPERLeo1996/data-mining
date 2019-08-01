from snownlp import SnowNLP

list = []


with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list.append(line)

for index in list:
    print(index)
    s = SnowNLP(index)
    print(s.sentiments)
