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
    # An index variable to indicate the language of current seed
    lang_index = 0

    for seed in seeds:
        report_filename = "reports{}.csv".format(seeds.index(seed) + 1)
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

        # professor wants us to go 500 to 1000 pages deep, with an absolute minimum of 100
        visited_pages = 0

        # iterate through the urls list
        # it constantly increases size (StackOverFlow says not to alter iterables when looping over them)
        index = 0

        while visited_pages < max_pages:
            url = urls[index]
            
            # if page can be crawled
            if robot.can_fetch("*", url):

                soup = make_request(session, url)
                
                # adding language to lang_list when crawling a new domain
                if index == 0:
                    lang_list.append(detect_language(soup))
                else:
                    # if the language of the outlink is different from the current language in the list
                    # skip crawling the page
                    # assume langdetect method is 100% accurate, but it may detect the wrong language and skip the page
                    if detect_language(soup) != lang_list[lang_index]:
                        continue

                visited_pages += 1
                
                # download current page and save to appropriate folder
                write_to_repository(folder, "page{}.txt".format(visited_pages), soup.prettify())

                write_to_word_count(word_count_filename, soup.get_text())

                # get all the domain links from current page and add seed url to hrefs
                # we also remove duplicates using a set then converting back to list
                outlinks = list(set([link.get('href') for link in soup.findAll('a') if link.get('href') is not None and "javascript" not in link.get('href')]))

                # Some links are full urls, others are hrefs so append the seed prefix to those
                # To know if some urls are complete or not, we check if they contain https, www or .com
                outlinks = [seed+link for link in outlinks if not any(s in link for s in ["https", "www", ".com", ".ac.kr", ".fr"])]

                # remove all links that would lead us outside the current domain
                outlinks = [link for link in outlinks if seed.removeprefix('https://www.') in link]

                # write url and outlinks count to relevant reports.csv
                write_links_count(url, len(outlinks), report_filename)

                # add new links at the end of urls list, as we will eventually scrape them as well
                # only if our list does not have more urls than max_pages
                if len(urls) < max_pages:
                    urls.extend(outlinks)

            index += 1

            # If we go through here, the domain might not have any more outlinks and we've visited all pages
            if index >= len(urls):
                break
        write_to_domain_count(word_count_filename, domain_word_count_filename)
            
        # go to the next seed
        lang_index += 1


def make_request(sesh, url):
    # headers are required for certain websites
    source_code = sesh.get(url, headers={'User-Agent': 'test_spider'})
    html_text = source_code.text
    source_code.close()
    soup = BeautifulSoup(html_text, features="html.parser")
    return soup


def build_session():
    session = requests.Session()
    # This helps ease off the servers we are crawling by waiting between subsequent requests
    retry = Retry(connect=3, backoff_factor=1.5)
    adapter = HTTPAdapter(max_retries=retry)
    # This will only request urls with https
    session.mount('https://', adapter)
    return session
