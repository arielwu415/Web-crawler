# -*- coding: utf-8 -*-
"""
Created on Sun May 1 15:27:04 2022

@author: Ariel
"""
import csv
import networkx as nx
import numpy as np


class pageRank:
    def __init__(self):
        self.pr = []
    
    def create_pageRank(self, filename):
        A, nodes = self.read_edge_list(filename)
        v = np.ones(nodes, 1) / nodes
        pA = self.probability_matrix(A)
        
        self.pr = self.get_pageRank(pA, v)
    
    def read_edge_list(self, filename):
        # read edge_list file and create a graph G
        with open(filename, "rb") as edges:
            G = nx.read_edgelist(edges, delimiter=",", create_using=nx.DiGraph, encoding="utf-8")

        # make an adjacency matrix
        A = nx.to_numpy_array(G)
        nodes = G.get_node_number()
        
        return A, nodes

    # A[:, 1] : second column
    # len(A[:,1]) <-- size of column

    def probability_matrix(self, A):
        for x in range(A.shape[1]):
            # counting number of page occurence
            count = np.count_nonzero(A == 1, axis=0)
            # print(count)

        for row in range(len(A)):
            for column in range(len(A[row])):
                # print("matrix value", A[row, column])
                # print("count", count[column])
                if count[column] != 0:
                    A[row, column] /= count[column]

        return A

        # numpy.savetxt("prob_matrix.csv", A, delimiter=",")
    
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
            if np.subtract(result, v).all() <= 0.0001:
                break

        return result
