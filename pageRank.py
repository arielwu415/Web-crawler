# -*- coding: utf-8 -*-
"""
Created on Sun May 1 15:27:04 2022

@author: Ariel
"""
import csv
import networkx as nx
import numpy as np
from outlinks_count import clear_report_file


class pageRank:
    
    def __init__(self):
        self.pr = []
        self.node_list = []
    
    
    def create_pageRank(self, filename):
        A, nodes = self.read_edge_list(filename)
        v = np.ones((nodes, 1)) / nodes
        pA = self.probability_matrix(A)
        
        self.pr = self.get_pageRank(pA, v)
    
    
    def read_edge_list(self, filename):
        G = nx.DiGraph()
        
        all_nodes = ["page{}".format(n+1) for n in range(len(self.node_list))]
        
        # read edge_list file and create a graph G
        with open(filename, "r") as edgecsv:
            edgereader = csv.reader(edgecsv)
            edges = [tuple(e) for e in edgereader][:]
        
        G.add_nodes_from(all_nodes)
        G.add_edges_from(edges)
        
        # make an adjacency matrix
        A = nx.to_numpy_array(G)
        A = np.transpose(A)

        nodes = G.number_of_nodes()
        self.node_list = list(G.nodes)
        return A, nodes


    def probability_matrix(self, A):
        # A[:, 1] : second column
        # len(A[:,1]) <-- size of column
        
        for x in range(A.shape[1]):
            # counting number of page occurrence
            count = np.count_nonzero(A == 1, axis=0)
            # print(count)

        for row in range(len(A)):
            for column in range(len(A[row])):
                # print("matrix value", A[row, column])
                # print("count", count[column])
                if count[column] != 0:
                    A[row, column] /= count[column]

        return A
    
    
    def get_pageRank(self, matrix, v):
        # First iteration:
        #     matrix        v      result
        # |[0.33 0.5 0]|   |v0|   |new_v0|
        # |[0.33  0  0]| x |v1| = |new_v1|
        # |[0.33 0.5 1]|   |v2|   |new_v2|

        # Second iteration:
        #     matrix           matrix        v      result
        # |[0.33 0.5 0]|   |[0.33 0.5 0]|   |v0|   |new_v0|
        # |[0.33  0  0]| x |[0.33  0  0]| x |v1| = |new_v1|
        # |[0.33 0.5 1]|   |[0.33 0.5 1]|   |v2|   |new_v2|
        #                  ^ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        #                 result from first iteration
        result = v

        # iterating until it converges
        while True:
            # current v = previous result
            v = result
            # calculate new result
            result = matrix.dot(v)

            # if result doesn't change much, break the loop
            if all(np.subtract(result, v) <= 0.000001):
                break

        return result
    
    
    def get_top_100(self):
        page = {"page{}".format(ID+1): self.pr[ID][0] for ID in range(len(self.node_list))}            
        sort_pages = sorted(page.items(), key=lambda x: x[1], reverse=True)
        
        for item in sort_pages[:100]:
            print(item[0], item[1])
        
        

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