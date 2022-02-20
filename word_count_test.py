from collections import Counter

from word_count import *

# tuple containing domain names for repository/{domain_directory}
directories = ('stackoverflow', 'coupang', 'gouvernement')

word_lists = get_wordlists(directories)

stackoverflow_word_count = get_word_count(word_lists[0])
coupang_word_count = get_word_count(word_lists[1])
gouvernement_word_count = get_word_count(word_lists[2])

# this is an example of how to get the top x most frequent words

counter = Counter(stackoverflow_word_count)
top_10_words = counter.most_common(10)
print(top_10_words)

