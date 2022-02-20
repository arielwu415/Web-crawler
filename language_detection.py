from bs4.element import Comment
from langdetect import detect, DetectorFactory
from iso639 import languages
import requests
from bs4 import BeautifulSoup


def detect_language(soup):
    # check if lang attribute exists
    if soup.html.has_attr('lang'):
        # slice the value [0:2]. For example, "ko-KR" get "ko"
        lang = soup.html['lang'][0:2]
        
        # use iso-639 code module to get the language name
        # lang = languages.get(alpha2=lang).name
        print(lang)
        return lang
    
    # if  attribute does not exist, detect content text
    else:
        # fix langdetect's unstable results
        DetectorFactory.seed = 0
        
        visible_txt = get_visible_text(soup)
        print(visible_txt)
        
        # use iso-639 code module to get the language name
        # lang = languages.get(alpha2=detect(visible_txt)).name
        lang = detect(visible_txt)
        print(lang)
        return lang


def tag_visible(element):
    if element.parent.name in ['head', 'title', 'meta', 'style', 'script', '[document]']:
        return False
    elif isinstance(element, Comment):
        return False
    else:
        return True


def get_visible_text(soup):
    txt = soup.findAll(text=True)
    # exclude unneeded tags
    filter_obj = filter(tag_visible, txt)
    
    visible_txt = str(u" ".join(t.strip() for t in filter_obj))
    return visible_txt


'''
source_code = requests.get("https://www.stackoverflow.com", headers={'User-Agent': 'test_spider'})
html_text = source_code.text
soup = BeautifulSoup(html_text, features="html.parser")
detect_language(soup)
'''

