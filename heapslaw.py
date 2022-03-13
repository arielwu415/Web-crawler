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

X_gouvernement = []
Y_gouvernement = []
num_words_gouvernement = 0
counter_dict_gouvernement = Counter()

X_coupang = []
Y_coupang = []
num_words_coupang = 0
counter_dict_coupang = Counter()

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

        num_words_gouvernement += len(words)
        X_gouvernement.append(num_words_gouvernement)

        temp_dict = get_word_count(words)
        counter_dict_gouvernement += Counter(temp_dict)
        Y_gouvernement.append(len(counter_dict_gouvernement))

with open('nocommaswordcount3.txt', 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()
    for index, line in enumerate(lines):
        if line == '\n':
            continue
        words = line.split(' ')
        words[-1].strip()

        num_words_coupang += len(words)
        X_coupang.append(num_words_coupang)

        temp_dict = get_word_count(words)
        counter_dict_coupang += Counter(temp_dict)
        Y_coupang.append(len(counter_dict_coupang))

stackoverflow_plot = sns.lineplot(x=X_stackoverflow, y=Y_stackoverflow)
stackoverflow_plot.set_xlabel('Words in Collection Stackoverflow')
stackoverflow_plot.set_ylabel('Words in Vocabulary Stackoverflow')
plt.show()

gouvernement_plot = sns.lineplot(x=X_gouvernement, y=Y_gouvernement)
gouvernement_plot.set_xlabel('Words in Collection Gouvernement')
gouvernement_plot.set_ylabel('Words in Vocabulary Gouvernement')
plt.show()

coupang_plot = sns.lineplot(x=X_coupang, y=Y_coupang)
coupang_plot.set_xlabel('Words in Collection Coupang')
coupang_plot.set_ylabel('Words in Vocabulary Coupang')
plt.show()