from indexer import Index

class SearchEngine():
    
    def __init__(self, index):
        ''' use Index instance as its argument'''
        self.index = index
        self.results = []

    
    def search(self, search_type = 'AND'):
        ''' search for term based on search type
        (only AND operator is required for this assignment)'''
        
        # get user input
        query = input("Please enter your query: ").lower()
        
        # clear results
        self.results = []
        
        # process term
        terms = query.split(" ")
        
        # get indexes and turn lists into sets of documents
        file_index = self.index.get_index()
        for i in file_index:
            file_index[i] = set(file_index[i])
        
        # perform set operations
        result_set = set()
        for term in terms:
            if term in file_index:
                if len(result_set) != 0:
                    result_set = result_set & file_index[term]
                else:
                    result_set = file_index[term]

        # print out results (unsorted)
        if search_type =='AND':
            
            self.results = list(result_set)
            result = "Relevant results are: "
            for doc in self.results:
                result += doc + " "
                
        print(result)
   

index = Index()
index.create_index("wordcount1.csv")
SE = SearchEngine(index)
SE.search()

index.create_index("wordcount2.csv")
SE = SearchEngine(index)
SE.search()

index.create_index("wordcount3.csv")
SE = SearchEngine(index)
SE.search()


