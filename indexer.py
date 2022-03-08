import pickle


def create_index():
    """ create a new index and save to file """
    file_index = {}

    with open('index.pkl', 'wb') as f:
        pickle.dump(file_index, f)
