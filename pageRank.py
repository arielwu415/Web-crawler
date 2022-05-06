# -*- coding: utf-8 -*-
"""
Created on Sun May 1 15:27:04 2022

@author: Ariel
"""
import csv
import networkx as nx


def create_edge_list(url_nodes):
    index = 0
    for node_set in url_nodes:
        index += 1
        filename = "edge_list{}.csv".format(index)
        for nodes in node_set:
            for i in range(len(nodes)):
                with open(filename, 'a', newline='') as report:
                    _writer = csv.writer(report)
                    _writer.writerow([nodes[0], nodes[i]])
                