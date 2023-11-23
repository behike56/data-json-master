import json
import matplotlib.pyplot as plt


data = json.load(open('json/pop.json', encoding='utf-8'))

x, totals, man, woman = [], [], [], []

for row in data:
    x.append(row['year'])
    totals.append(row['total'])
    man.append(row['man'])
    woman.append(row['woman'])

p_total = plt.plot(x, totals, label='合計(千人)')
p_woman = plt.plot(x, woman, marker='.', label='女')
p_man = plt.plot(x, man, marker='x', label='男')

plt.legend()
plt.show()
