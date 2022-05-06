import os
import pickle
import csv


class Index:
    def __init__(self):
        self.file_index = {}
        self.documents_count = 0

    def create_index(self, filename):
        """ create a new index and save to index.pkl file """

        # Reset instance variables just in case they still hold non-empty references, might not be necessary though
        self.file_index = {}
        self.documents_count = 0
        
        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                index = 0
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        index += 1
                        for word in row:
                            if word not in self.file_index:
                                self.file_index[word] = [(f"doc{index}", 1)]
                            else:
                                term_docs = self.file_index[word]
                                output = list(filter(lambda x: f"doc{index}" in x, term_docs))
                                if not output:
                                    self.file_index[word].append((f"doc{index}", 1))
                                else:
                                    self.file_index[word].remove(output[0])
                                    self.file_index[word].append((f"doc{index}", output[0][1]))
                self.documents_count = index

        with open('index.pkl', 'wb') as f:
            pickle.dump(self.file_index, f)

    def load_index(self, name):
        """ load index if it exists"""
        try:
            with open(name, 'rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_index = {}

    def get_index(self):
        return self.file_index
