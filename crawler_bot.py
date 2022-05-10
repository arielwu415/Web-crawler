# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 16:28:04 2022

@author: Ariel
@author: Clarence
@author: Yeonah
"""
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import ssl
from bs4 import BeautifulSoup
from outlinks_count import *
from download_page import *
from language_detection import detect_language
import urllib.robotparser


def crawler_bot(seeds, max_pages):
    # One session will be active for all requests, as opposed to creating a new one at every iteration
    session = build_session()

    ssl._create_default_https_context = ssl._create_unverified_context
    
    # A list to store language names as strings
    # for checking if each page we crawl is in the same language as the seed
    # In our case, lang_list = ["en", "fr", "ko"]
    lang_list = []
    # An index.pkl variable to indicate the language of current seed
    lang_index = 0
    
    seed_edges = []
    for seed in seeds:
        report_filename = "report{}.csv".format(seeds.index(seed) + 1)
        clear_report_file(report_filename)

        word_count_filename = "wordcount{}.csv".format(seeds.index(seed) + 1)
        clear_report_file(word_count_filename)

        domain_word_count_filename = "words{}.csv".format(seeds.index(seed) + 1)
        clear_report_file(domain_word_count_filename)

        folder = get_folder_name(seed)

        # concat robots.txt to domain url
        robot_url = seed + "/robots.txt"
        
        # parsing robots.txt
        robot = urllib.robotparser.RobotFileParser()
        robot.set_url(robot_url)
        robot.read()
        
        # all the urls for the current domain (eng, fr, kr)
        urls = [seed]
        edges = []
        
        # professor wants us to go 500 to 1000 pages deep, with an absolute minimum of 100
        visited_pages = 0
        
        # create pageID dictionary to store url as a key and ID as a value
        # eg. {"https://www.stackoverflow.com": "page1"
        #       "https://www.stackoverflow.com/teams/pricing": "page2"}
        pageID = {}
        
        # iterate through the urls list
        # it constantly increases size (StackOverFlow says not to alter iterables when looping over them)
        index = 0
        
        while visited_pages < max_pages:
            url = urls[index]
            
            # if page can be crawled
            if robot.can_fetch("*", url):

                soup = make_request(session, url)  # soup can be null, case might not be properly handled
                
                lang = detect_language(soup)
                if index == 0:
                    # adding language to lang_list when crawling a new domain
                    lang_list.append(lang)
                else:
                    # if the language of the outlink is different from the current language in the list
                    # skip crawling the page
                    # assume langdetect method is 100% accurate, but it may detect the wrong language and skip the page
                    if lang != lang_list[lang_index]:
                        print(url)
                        continue

                visited_pages += 1
                neighbors = [url]
                
                pageID[url] = "page{}".format(visited_pages)
                
                # download current page and save to appropriate folder
                write_to_repository(folder, "page{}.txt".format(visited_pages), soup.prettify())

                write_to_word_count(word_count_filename, soup.get_text())

                # get all the domain links from current page and add seed url to hrefs
                # we also remove duplicates using a set then converting back to list
                outlinks = list(set([link.get('href') for link in soup.findAll('a') if link.get('href') is not None and "javascript" not in link.get('href')]))

                outlinks = [link for link in outlinks if not any(s in link for s in ["backslash", "tagged", "javascript", "jobs", ".org"])]
                
                # Some links are full urls, others are hrefs so append the seed prefix to those
                # To know if some urls are complete or not, we check if they contain https, www or domain extensions
                outlinks = [seed+link for link in outlinks if not any(s in link for s in ["https", "www", ".com", ".ac.kr", ".fr"])]
                
                # remove all links that would lead us outside the current domain.
                # This also removes the seed url if it is put back in the list. We don't need to parse it again
                outlinks = [link for link in outlinks if seed.removeprefix('https://www.') in link and link != seed]
                
                # write url and outlinks count to relevant reports.csv
                write_links_count(url, len(outlinks), report_filename)
                
                # add new links at the end of urls list, as we will eventually scrape them as well
                # only if our list does not have more urls than max_pages
                if len(urls) < max_pages:
                    unique = [link for link in outlinks if link not in urls]
                    urls.extend(unique)
                    
                    neighbors.extend(outlinks)
                    edges.append(neighbors)

            index += 1

            # If we go through here, the domain might not have any more outlinks and we've visited all pages
            if index >= len(urls):
                break
        breakpoint()
        write_to_domain_count(word_count_filename, domain_word_count_filename)
        
        lang_index += 1
        edges_ID = [[pageID[link] for link in links if link in pageID] for links in edges]
        
        # go to the next seed
        seed_edges.append(edges_ID)
        
    return seed_edges


def make_request(sesh, url):
    soup = None
    # headers are required for certain websites
    try:
        source_code = sesh.get(url, headers={'User-Agent': 'test_spider'})

        html_text = source_code.text
        source_code.close()
        soup = BeautifulSoup(html_text, features="html.parser")
    except:
        print("Error in make_request")
    return soup


def build_session():
    session = requests.Session()
    # This helps ease off the servers we are crawling by waiting between subsequent requests
    retry = Retry(connect=5, backoff_factor=5)
    adapter = HTTPAdapter(max_retries=retry)
    # This will only request urls with https
    session.mount('https://', adapter)
    return session
