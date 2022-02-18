import requests
from bs4 import BeautifulSoup


def get_test_soup(url):
    source_code = requests.get(url, headers={'User-Agent': 'test_spider'})
    html_text = source_code.text
    soup = BeautifulSoup(html_text, features="html.parser")

    return soup


def run_test(fcn, arg):
    print(fcn(arg))
