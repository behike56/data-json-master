import json
import japanize_matplotlib
import matplotlib.pyplot as plt

data = json.load(open('json/pi.json', encoding='utf-8'))

values = [i[0] for i in data]
labels = [i[1] for i in data]

plt.pie(values, labels=labels)
plt.show()
