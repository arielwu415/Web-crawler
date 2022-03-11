class SearchEngine():
    
    def __init__(self, index):
        ''' use Index instance as its argument'''
        self.index = index
        self.results = []
    
    def search(self, query, search_type = 'AND'):
        ''' search for term based on search type
        (only AND operator is required for this assignment)'''
        
        # clear results
        self.results = []
        
        
        # process term
        # example: ["tropical", "fish"]
        terms = query.split(" ")
        
        
        # search from index
        # example:
        # { "tropical": ["doc1", "doc2", "doc5", ...],
        #   "fish": ["doc2", "doc3", ...], ... }
        file_index = self.index.get_index()
        
        
        # create dictionary to count number terms existing in doc_n
        # example:
        # {'doc1': 1, 'doc2': 2, 'doc5': 2, 'doc3': 1}
        docs = {}
        for term in terms:
            # if term exists in file_index
            if term.lower() in file_index:
                # iterate through ["doc1", "doc2", "doc5", ...]
                for n in file_index[term]:
                    if n not in docs:
                        docs[n] = 1
                    else:
                        docs[n] += 1

        if search_type =='AND':
            self.results = [n for n in docs if docs[n] == len(terms)]
            print(query, self.results)

        

'''Testing'''
class Index():
    
    def __init__(self):
        self.index = {"tropical": ["doc1", "doc2", "doc5"],
                      "fish": ["doc2", "doc3", "doc5"],
                      "hi": ["doc2", "doc5"] }
        
    def get_index(self):
        return self.index

index = Index()
SE = SearchEngine(index)
SE.search("tropical") # tropical ['doc1', 'doc2', 'doc5']
SE.search("tropical fish") # tropical fish ['doc2', 'doc5']
