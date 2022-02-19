from bs4.element import Comment
from langdetect import detect, DetectorFactory
from iso639 import languages
from crawler_bot import get_soup

lang_dict = {"ko":"Korean",
             "en":"English",
             "fr":"French"}


def detect_language(soup):
    # check if lang attribute exists
    if soup.html.has_attr('lang'):
        # slice the value [0:2]. For example, "ko-KR" get "ko"
        lang = soup.html['lang'][0:2]
        
        # use iso-639 code module to get the language name
        lang = languages.get(alpha2=lang).name
        return lang
    
    # if  attribute does not exist, detect content text
    else:
        # fix langdetect's unstable results
        DetectorFactory.seed = 0
    
        txt = soup.findAll(text=True)
        # exclude unneeded tags
        filtered_txt = filter(tag_visible, txt)
        
        visible_txt = str(u" ".join(t.strip() for t in filtered_txt))
        
        # use iso-639 code module to get the language name
        lang = languages.get(alpha2=detect(visible_txt)).name
        return lang


def tag_visible(element):
    if element.parent.name in ['head', 'title', 'meta', 'style', 'script', '[document]']:
        return False
    elif isinstance(element, Comment):
        return False
    else:
        return True


s = get_soup("https://www.coupang.com/")
