# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:28:04 2022

@author: Ariel
"""
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

from langdetect import detect


def crawler_bot():
    url = "https://www.coupang.com/"
    
    # hearders are required for https://www.coupang.com/
    source_code = requests.get(url, headers = {'User-Agent':'test'})
    html = source_code.text
    soup = BeautifulSoup(html)
    
    return soup
    

def detect_language(soup):
    # search for <html lang="...">
    # if attribute exists, return lang value
    # incomplete
    
    
    # if not exist, detect content text
    txt = soup.findAll(text = True)
    visible_txt = filter(tag_visible, txt) # exclude unneeded tags
    
    lan = detect(u" ".join(t.strip() for t in visible_txt))
    return lan


def tag_visible(element):
    if element.parent.name in ['head', 'title', 'meta', 'style', 'script', '[document]']:
        return False
    elif isinstance(element, Comment):
        return False
    else:
        return True
    
    
soup_obj = crawler_bot()
print(detect_language(soup_obj))