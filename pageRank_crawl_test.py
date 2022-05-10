from crawler_bot import crawler_bot
from pageRank import create_edge_list

links = ["https://www.stackoverflow.com", "https://www.lemonde.fr", "https://www.wconcept.co.kr"]

seed_edges = crawler_bot(links, 500)

create_edge_list(seed_edges)