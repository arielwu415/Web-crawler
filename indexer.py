import os
import pickle
import csv


class Index:
    def __init__(self):
        self.file_index = {}

    def create_index(self, filename):
        """ create a new index and save to index.pkl file """
        
        self.file_index = {}
        
        if os.path.isfile(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                index = 0
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        index += 1
                        for word in row:
                            if word not in self.file_index:
                                self.file_index[word] = [f"doc{index}"]
                            else:
                                if f"doc{index}" not in self.file_index[word]:
                                    self.file_index[word].append(f"doc{index}")

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
