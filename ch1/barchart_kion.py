import csv
import matplotlib.pyplot as plt

reader = csv.reader(open('csv/kion_data.csv', encoding='utf-8'))
data = list(reader)

labels = data[0]
temps = [float(v) for v in data[1][1:]]

plt.bar(labels, temps)
plt.title('最高気温')

plt.show()
