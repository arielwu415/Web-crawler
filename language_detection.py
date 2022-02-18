from bs4.element import Comment
from langdetect import detect, DetectorFactory
from tests import *


def detect_language(soup):
    # search for <html lang="...">
    # if attribute exists, return lang value
    # incomplete
    DetectorFactory.seed = 0

    # if not exist, detect content text
    txt = soup.findAll(text=True)
    visible_txt = filter(tag_visible, txt)  # exclude unneeded tags
    
    lan = detect(u" ".join(t.strip() for t in visible_txt))
    return lan


def tag_visible(element):
    if element.parent.name in ['head', 'title', 'meta', 'style', 'script', '[document]']:
        return False
    elif isinstance(element, Comment):
        return False
    else:
        return True


s = get_test_soup("https://www.coupang.com/")
run_test(detect_language, s)
