# -*- coding: utf-8 -*-
"""
Created on Sun May 1 15:27:04 2022

@author: Ariel
"""
import csv
import networkx as nx
import numpy 
import numpy as np
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


def get_pageRank(matrix, vector):
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
    
    # trun vector into numpy ndarray object
    v = numpy.array(vector).reshape(len(vector), 1)
    result = v
    
    # iterating until it converges
    while True:
        # current v = previous result
        v = result
        # calculate new result
        result = matrix.dot(v)
        
        # if result doesn't change much, break the loop
        if numpy.subtract(result, v).all() <= 0.0001:
            break
    
    return result
    



# read edge_list file and create a graph G
with open("edge_list1.csv", "rb") as edges:
    G = nx.read_edgelist(edges, delimiter=",", create_using=nx.DiGraph, encoding="utf-8")
    
# make an adjacency matrix
A = nx.to_numpy_array(G)
print(A)

print(nx.info(G))

'''
# matrix is the probablity matrix based on the edges between pages
# v is the initial probability that each page has
def get_pageRank(matrix, v):
    
    # define how many iterations we want it to calculate
    # will check if the values converge later
    times = 30
    
    while times > 0:
        # create a copy of vector
        # new_v will store the matrix-vector results later
        new_v = v
                
        # counter for index of new_v
        count = 0
        for row in matrix:
            # initialize vector values
            v = new_v
            # in iteration each row set counter  vector to 0
            i = 0
            score = 0
            # each page will multiply with the value in vector[i]
            for page in row:
                score += page * v[i]
                i += 1
            # store the score in new_v
            new_v[count] = score
            # go to next row
            count += 1
        times -= 1
    
    return new_v
'''

# A[:, 1] : second column
# len(A[:,1]) <-- size of column


for x in range(A.shape[1]):
    #counting number of page occurence
    count = np.count_nonzero(A == 1, axis = 0)
    #print(count)
            
print(count)
    
for row in range(len(A)):
    for column in range(len(A[row])):
        print("matrix value", A[row,column])
        print("count", count[column])
        if (count[column] != 0):
            A[row,column] /= count[column]
        
print(A)
    
#numpy.savetxt("prob_matrix.csv", A, delimiter=",")

    