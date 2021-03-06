import csv
import json

from word_count import *


def write_links_count(link, count, filename):
    with open(filename, 'a', newline='') as report:
        _writer = csv.writer(report)
        _writer.writerow([link, count])


def write_to_word_count(filename, page):
    with open(filename, 'a', encoding='utf-8') as word_count_file:
        _writer = csv.writer(word_count_file)
        _writer.writerow(get_wordlist(page))


def write_to_domain_count(word_count_filename, domain_word_count_filename):
    all_words = []
    with open(word_count_filename, encoding='utf-8') as word_count_file:
        lines = word_count_file.readlines()
        for line in lines:
            if line == '\n':
                continue
            words = line.lower().split(',')
            cleaned_words = clean_words(words)
            all_words.extend(cleaned_words)
    
    with open(domain_word_count_filename, 'w', encoding='utf-8') as domain_word_count_file:
        _writer = csv.writer(domain_word_count_file)
        word_count = get_word_count(all_words)
        sorted_word_count_tuple = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
        for tup in sorted_word_count_tuple:
            _writer.writerow([tup[0], tup[1]])


def clear_report_file(filename):
    with open(filename, 'w', newline='') as report:
        report.close()
