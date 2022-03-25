"""
@author: Yeonah
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

x_stackOverFlow = []
y_stackOverFlow = []
x_lemonde = []
y_lemonde = []
x_yonsei = []
y_yonsei = []
count1 = 1
count2 = 1
count3 = 1

#StackOverFlow
with open('words1.csv', 'r', encoding='utf-8') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        if row:
            x_stackOverFlow.append(count1)
            y_stackOverFlow.append(row[1])
            count1 += 1
            

plt.plot(x_stackOverFlow, y_stackOverFlow)
plt.title('Zifs law for StackOverFlow')
plt.xlabel('Rank (most frequent word to least)')
plt.ylabel('Frequency (number of word appeared)')
plt.grid()
plt.yticks([0, 100, 200, 300, 400, 500, 589])
ax = plt.gca()
ax.invert_yaxis()
plt.show()

#Lemonde
with open('words2.csv', 'r', encoding='utf-8') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        if row:
            x_lemonde.append(count2)
            y_lemonde.append(row[1])
            count2 += 1

plt.plot(x_lemonde, y_lemonde)
ax = plt.gca()
ax.invert_yaxis()
plt.yticks([0, 100, 200, 300, 400, 500, 600, 712])
plt.title('Zifs law for Lemonde')
plt.xlabel('Rank (most frequent word to least)')
plt.ylabel('Frequency (number of word appeared)')
plt.grid()
plt.show()

#Yonsei
with open('words3.csv', 'r', encoding='utf-8') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        if row:
            x_yonsei.append(count3)
            y_yonsei.append(row[1])
            count3 += 1

plt.plot(x_yonsei, y_yonsei)
ax = plt.gca()
ax.invert_yaxis()
plt.title('Zifs law for Yonsei')
plt.xlabel('Rank (most frequent word to least)')
plt.ylabel('Frequency (number of word appeared)')
plt.grid()
plt.show()