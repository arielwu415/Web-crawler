# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 22:49:10 2022

@author: yeonah
"""

import requests
import urllib.robotparser
from bs4 import BeautifulSoup

url = "https://www.coupang.com/"
robot_url = url + "robots.txt"
robot = urllib.robotparser.RobotFileParser()
robot.set_url(robot_url)
robot.read()

request = requests.get(url, headers={'User-Agent': "test_spider"})
if (robot.can_fetch("*", url)):   #url needs to be changed to include all urls in domain
    response = urllib.urlopen(request)
