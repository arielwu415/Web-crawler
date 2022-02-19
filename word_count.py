from collections import Counter

# pass a list of strings, where each string is one of the text files
# where each word in the text file is separated by spaces.
# Since we're getting the word counts of each domain, rather than each
# individual page, I assume that I can just combine the word counts of all
# the pages for a given domain. But let me know if I need to use different parameters
def get_wordlist(pages):
    word_list = []
    for page in pages:
        # creates a list of words from the page assuming the words are
        # separated by spaces. Then remove unwanted symbols as well.
        words = page.lower().split()
        cleaned_words = clean_words(words)
        for word in cleaned_words:
            if word not in word_list:
                word_list.append(word)

    return word_list


def clean_words(words):
    cleaned_words = []
    for word in words:
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

        for i in range(len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            cleaned_words.append(word)

    return cleaned_words

# creates a dictionary where each key is a unique word
# and each value is the count of that respective word
def get_word_count(word_list):
    word_count = {}

    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # this is an example of how to get the top 100 most frequent words
    counter = Counter(word_count)

    top_100_words = counter.most_common(100)
    print(top_100_words)

    return word_count