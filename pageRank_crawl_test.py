from crawler_bot import crawler_bot
from pageRank import *

links = ["https://www.stackoverflow.com", "https://www.lemonde.fr", "https://www.wconcept.co.kr"]

seed_edges = crawler_bot(links, 600)

create_edge_list(seed_edges)