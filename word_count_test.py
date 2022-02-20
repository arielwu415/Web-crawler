from collections import Counter

from word_count import *

# tuple containing domain names for repository/{domain_directory}
directories = ('stackoverflow', 'coupang', 'gouvernement')

# gets the word lists for each domain returned as a list of lists
# e.g. [ ['stack', 'overflow', 'words'], ['coupang', 'words'], ['gouvernement', 'words'] ]
word_lists = get_wordlists(directories)

# each of these is a dictionary for each domain. 
# in each dictionary, each key is a unique word
# and each value is the count of that respective word
stackoverflow_word_count = get_word_count(word_lists[0])
coupang_word_count = get_word_count(word_lists[1])
gouvernement_word_count = get_word_count(word_lists[2])

# this is an example of how to get the top x most frequent words

counter = Counter(stackoverflow_word_count)
top_10_words = counter.most_common(10)
print("Top 10 most common words from stack overflow:")
print(top_10_words)

