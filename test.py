from word_count import *

all_words = []

with open('./repository/stackoverflow/page1.txt', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        if line == '\n':
            continue
        words = line.lower().split()
        cleaned_words = clean_words(words)
        all_words.extend(cleaned_words)
print(all_words)