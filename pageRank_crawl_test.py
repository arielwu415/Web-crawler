from crawler_bot import crawler_bot
from pageRank import *

links = ["https://www.stackoverflow.com", "https://www.lemonde.fr", "https://www.wconcept.co.kr/"]

url_nodes = crawler_bot(links, 30)

create_edge_list(url_nodes)