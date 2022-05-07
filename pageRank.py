# -*- coding: utf-8 -*-
"""
Created on Sun May 1 15:27:04 2022

@author: Ariel
"""
import csv
import networkx as nx
from outlinks_count import clear_report_file

def create_edge_list(seed_edges):
    index = 0
    for node_sets in seed_edges:
        index += 1
        filename = "edge_list{}.csv".format(index)
        clear_report_file(filename)
        for nodes in node_sets:
            center_node = nodes[0]
            neighbors = list(set(nodes[1:]))
            for i in range(len(neighbors)):
                with open(filename, 'a', newline='', encoding="utf-8") as csvfile:
                    _writer = csv.writer(csvfile)
                    _writer.writerow([center_node, neighbors[i]])

lst = [[["hello", "world", "I", "hate", "you"], ["I", "hate", "this", "too"], ["work", "harder"]]]
create_edge_list(lst)

# read edge_list file and create a graph G
with open("edge_list1.csv", "rb") as edges:
    G = nx.read_edgelist(edges, delimiter=",", encoding="utf-8")
    
# make an adjacency matrix
A = nx.adjacency_matrix(G)