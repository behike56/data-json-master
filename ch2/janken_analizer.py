import json
# import japanize_matplotlib
import matplotlib.pyplot as plt


save_file = 'janken_history.json'
with open(save_file, encoding='utf-8') as fp:
    history = json.load(fp)


win, lose, draw = 0, 0, 0
hand = [0, 0, 0]

for i in history:
    if i['result'] == 'EVEN':
        draw += 1
    
    if i['result'] == 'LOSE':
        lose += 1
    
    if i['result'] == 'WIN':
        win += 1
        hand[i['user']] += 1
    
print('WIN RATE:', win / (win + lose))

plt.subplot(1, 2, 1)
plt.pie([win, lose, draw], labels=['WIN', 'LOSE', 'DRAW'], autopct="%1.1f %%")
plt.title('WIN RATE')

plt.subplot(1, 2, 2)
plt.barh(['グー', 'チョキ', 'パー'], hand)
plt.title('どの手で勝ったか')

plt.show()
import requests, os, time, json
import urllib.parse
from bs4 import BeautifulSoup