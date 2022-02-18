# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:28:04 2022

@author: Ariel
@author: Clarence
"""

import requests
from bs4 import BeautifulSoup
from outlinks_count import write_links_count


def crawler_bot(seeds, max_pages):
    for seed in seeds:
        # all the urls for the current domain (eng, fr, kr)
        urls = [seed]

        # professor wants us to go 500 to 1000 pages deep, with an absolute minimum of 100
        visited_pages = 0

        # iterate through the urls list
        # it constantly increases size (StackOverFlow says not to alter iterables when looping over them)
        index = 0

        while visited_pages < max_pages:
            url = urls[index]
            visited_pages += 1

            # headers are required for https://www.coupang.com/
            soup = get_soup(url)

            # get all the domain links from current page and add seed url to hrefs
            # we also remove duplicates using a set then converting back to list
            outlinks = list(set([link.get('href') for link in soup.findAll('a') if link.get('href') is not None]))

            # this next line of code gets links to different domains, not sure if we need to crawl those
            # outlinks.extend([link.get('href') for link in soup.findAll('link')])

            # Some links are full urls, others are hrefs so append the seed prefix to those
            # To know if some urls are complete or not, we check if they contain https or www
            outlinks = [seed + link for link in outlinks if not any(s in link for s in ["https", "www"])]

            # write url and outlinks count to relevant reports.csv
            write_links_count(url, len(outlinks), "reports{}.csv".format(seeds.index(seed) + 1))

            # add new links at the end of urls list, as we will eventually scrape them as well
            # only if our list does not have more urls than max_pages
            if len(urls) < max_pages:
                urls.extend(outlinks)

            index += 1

            # If we go through here, the domain might not have any more outlinks and we've visited all pages
            if index >= len(urls):
                break

def get_soup(url):
    source_code = requests.get(url, headers={'User-Agent': 'test_spider'})
    html_text = source_code.text
    soup = BeautifulSoup(html_text, features="html.parser")
    
    return soup
    

links = ["https://www.coupang.com/"]
crawler_bot(links, 10)
