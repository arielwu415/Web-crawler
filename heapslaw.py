from collections import Counter

import matplotlib.pyplot as plt
import seaborn as sns

from nocommas import make_text_files_no_commas
from word_count import get_word_count

sns.set_theme()

X_stackoverflow = []
Y_stackoverflow = []
num_words_stackoverflow = 0
counter_dict_stackoverflow = Counter()

X_lemonde = []
Y_lemonde = []
num_words_lemonde = 0
counter_dict_lemonde = Counter()

X_yonsei = []
Y_yonsei = []
num_words_yonsei = 0
counter_dict_yonsei = Counter()

make_text_files_no_commas()

with open('nocommaswordcount1.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()
    for index, line in enumerate(lines):
        if line == '\n':
            continue
        words = line.split(' ')
        words[-1].strip()

        num_words_stackoverflow += len(words)
        X_stackoverflow.append(num_words_stackoverflow)

        temp_dict = get_word_count(words)
        counter_dict_stackoverflow += Counter(temp_dict)
        Y_stackoverflow.append(len(counter_dict_stackoverflow))

with open('nocommaswordcount2.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()
    for index, line in enumerate(lines):
        if line == '\n':
            continue
        words = line.split(' ')
        words[-1].strip()

        num_words_lemonde += len(words)
        X_lemonde.append(num_words_lemonde)

        temp_dict = get_word_count(words)
        counter_dict_lemonde += Counter(temp_dict)
        Y_lemonde.append(len(counter_dict_lemonde))

with open('nocommaswordcount3.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()
    for index, line in enumerate(lines):
        if line == '\n':
            continue
        words = line.split(' ')
        words[-1].strip()

        num_words_yonsei += len(words)
        X_yonsei.append(num_words_yonsei)

        temp_dict = get_word_count(words)
        counter_dict_yonsei += Counter(temp_dict)
        Y_yonsei.append(len(counter_dict_yonsei))

stackoverflow_plot = sns.lineplot(x=X_stackoverflow, y=Y_stackoverflow)
stackoverflow_plot.set_xlabel('Total Words in Collection Stackoverflow')
stackoverflow_plot.ticklabel_format(style='plain', axis='x')
stackoverflow_plot.set_ylabel('Unique Words in Vocabulary Stackoverflow')
plt.show()

lemonde_plot = sns.lineplot(x=X_lemonde, y=Y_lemonde)
lemonde_plot.set_xlabel('Total Words in Collection Lemonde')
stackoverflow_plot.ticklabel_format(style='plain', axis='x')
lemonde_plot.set_ylabel('Unique Words in Vocabulary Lemonde')
plt.show()

yonsei_plot = sns.lineplot(x=X_yonsei, y=Y_yonsei)
yonsei_plot.set_xlabel('Total Words in Collection Yonsei')
yonsei_plot.set_ylabel('Unique Words in Vocabulary Yonsei')
plt.show()