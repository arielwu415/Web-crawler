# -*- coding: utf-8 -*-
"""
Created on Sun May 1 15:27:04 2022

@author: Ariel
"""

import pandas as pd
import networkx as nx

def read_csv_file(file_name, num):
    # read data from "reports.csv" file
    df = pd.read_csv("{0}{1}.csv".format(file_name, num))
    
    # get the fist column and make it a set to prevent duplicates
    urls_from_csv = list(set(df.iloc[:, 0]))
    
    return urls_from_csv
    