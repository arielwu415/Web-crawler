import math

from indexer import Index
from pageRank import pageRank


class SearchEngine:
    def __init__(self, index, page_ranks):
        """ use Index instance as its argument """
        self.index = index
        self.page_ranks = page_ranks
        self.results = []

    def search(self, search_type='BM25'):
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
            qf = [terms.count(term) for term in terms]  # query frequency
            df = [len(file_index[term]) for term in terms]  # document frequency
            r, R = 0, 0  # No relevance information
            k1 = 1.2
            k2 = 100
            b = 0.75
            K = k1 * ((1 - b) + b * 0.9)  # Assume dl is 90% of avdl
            N = self.index.documents_count
            # print(qf, n, r, R, k1, k2, b, K, N)

            for i, term in enumerate(terms):
                docs = file_index[term]
                for doc, f in docs:
                    approximation = ((r + 0.5) / (R - r + 0.5)) / ((df[i] - r + 0.5) / (N - df[i] - R + r + 0.5))
                    modifier1 = (k1 + 1) * f / (K + f)
                    modifier2 = (k2 + 1) * qf[i] / (k2 + qf[i])
                    score = round(math.log(approximation) * modifier1 * modifier2, 5)  # Taking natural log

                    if doc in scores:
                        scores[doc] += score
                    else:
                        scores[doc] = score
            ranked_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}

        for key in ranked_scores:
            ranked_scores[key] *= self.page_ranks.pr[int(key.removeprefix('doc')) - 1]

        results = list(reversed(ranked_scores.keys()))
        breakpoint()
        # print out results (unsorted)
        self.results = list(results)
        documents = "Relevant documents are: "
        for doc in self.results:
            documents += doc + " "

        return documents
   

index = Index()
pageRank = pageRank()
pageRank.create_pageRank("edge_list1.csv")
index.create_index("wordcount1.csv")
SE = SearchEngine(index, pageRank)
print(SE.search())

index.create_index("wordcount2.csv")
SE = SearchEngine(index)
print(SE.search())

index.create_index("wordcount3.csv")
SE = SearchEngine(index)
print(SE.search())
