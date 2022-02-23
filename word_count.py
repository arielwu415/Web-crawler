# tuple containing domain names for repository/{domain_directory}
directories = ('stackoverflow', 'coupang', 'gouvernement')

# gets the word list for the page passed
# page is assumed to be soup.getText()
def get_wordlist(page):
    word_list = []
    lines = page.splitlines()
    for line in lines:
        if line == '\n':
            continue
        words = line.lower().split()
        cleaned_words = clean_words(words)
        word_list.extend(cleaned_words)

    return word_list

# removes unwanted symbols from a list of words (strings)
def clean_words(words):
    cleaned_words = []
    # for each word replace all unwanted symbols in that word with 
    # a blank space (empty string)
    for word in words:
        # all the unwanted symbols
        symbols = "!@#$%^&*()_-+={[}]|\;:\"<>«»?/.,… "
        
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

    return word_count
