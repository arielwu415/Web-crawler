import math

from indexer import Index


class SearchEngine:
    def __init__(self, index):
        """ use Index instance as its argument """
        self.index = index
        self.results = []

    def search(self, domain_size, search_type='BM25'):
        """ search for term based on search type
        (only AND operator is required for this assignment) """
        
        # get user input
        query = input("Please enter your query: ").lower()
        
        # clear results
        self.results = []
        
        # process term
        terms = query.split(" ")
        
        # get indices and turn lists into sets of documents
        file_index = self.index.get_index()
        for i in file_index:
            file_index[i] = set(file_index[i])

        results = set()

        if search_type == 'BOOLEAN':
            # perform set operations
            for term in terms:
                if term in file_index:
                    if len(results) != 0:
                        docs = file_index[term]
                        results = results & set([doc[0] for doc in docs])
                    else:
                        docs = file_index[term]
                        results = set([doc[0] for doc in docs])
        elif search_type == 'BM25':
            scores = {}
            qf = [terms.count(term) for term in terms]
            n = [len(file_index[term]) for term in terms]
            r, R = 0, 0  # No relevance information
            k1 = 1.2
            k2 = 100
            b = 0.75
            K = k1 * ((1 - b) + b * 0.9)  # Assume dl is 90% of avdl
            N = domain_size
            # print(qf, n, r, R, k1, k2, b, K, N)

            for i, term in enumerate(terms):
                docs = file_index[term]
                for doc, f in docs:
                    approximation = ((r + 0.5) / (R - r + 0.5)) / ((n[i] - r + 0.5) / (N - n[i] - R + r + 0.5))
                    modifier1 = (k1 + 1) * f / (K + f)
                    modifier2 = (k2 + 1) * qf[i] / (k2 + qf[i])
                    score = round(math.log(approximation) * modifier1 * modifier2, 5)
                    if doc in scores:
                        scores[doc] += score
                    else:
                        scores[doc] = score
            ranked_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}
            print(ranked_scores)


        # <--  Multiply page ranks with BM25 scores -->

        results = list(reversed(ranked_scores.keys()))
        print(results)
        breakpoint()

        # print out results (unsorted)
        self.results = list(results)
        documents = "Relevant documents are: "
        for doc in self.results:
            documents += doc + " "

        return documents
   

index = Index()
index.create_index("wordcount1.csv")
SE = SearchEngine(index)
print(SE.search(index.documents_count))
quit()

index.create_index("wordcount2.csv")
SE = SearchEngine(index)
print(SE.search(index.documents_count))

index.create_index("wordcount3.csv")
SE = SearchEngine(index)
print(SE.search(index.documents_count))


