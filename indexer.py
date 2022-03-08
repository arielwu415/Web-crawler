import os
import pickle
import csv


class Index:
    def __init__(self):
        self.file_index = {}

    def create_index(self):
        """ create a new index and save to index.pkl file """

        if os.path.isfile('wordcount1.csv'):
            with open('wordcount1.csv', 'r') as file1:
                index = 0
                reader = csv.reader(file1)
                for row in reader:
                    if row:
                        index += 1
                        for word in row.split(','):
                            if self.file_index[word]:
                                if f"doc{index}" not in self.file_index[word]:
                                    self.file_index[word].append(f"doc{index}")
                            else:
                                self.file_index[word] = [f"doc{index}"]

        if os.path.isfile('wordcount2.csv'):
            with open('wordcount2.csv', 'r') as file2:
                index = 0
                reader = csv.reader(file2)
                for row in reader:
                    if row:
                        index += 1
                        for word in row.split(','):
                            if self.file_index[word]:
                                if f"doc{index}" not in self.file_index[word]:
                                    self.file_index[word].append(f"doc{index}")
                            else:
                                self.file_index[word] = [f"doc{index}"]

        if os.path.isfile('wordcount3.csv'):
            with open('wordcount3.csv', 'r') as file3:
                index = 0
                reader = csv.reader(file3)
                for row in reader:
                    if row:
                        index += 1
                        for word in row.split(','):
                            if self.file_index[word]:
                                if f"doc{index}" not in self.file_index[word]:
                                    self.file_index[word].append(f"doc{index}")
                            else:
                                self.file_index[word] = [f"doc{index}"]

        with open('index.pkl', 'wb') as f:
            pickle.dump(self.file_index, f)

    def load_index(self, name):
        """ load index if it exists"""
        try:
            with open(name, 'rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_index = {}
