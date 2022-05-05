from crawler_bot import crawler_bot
from pageRank import read_csv_file

seeds = ["https://www.stackoverflow.com", "https://www.lemonde.fr", "https://www.yonsei.ac.kr/sc"]
crawler_bot(seeds, 3, 1, 1)

# after each crawl from seeds, read report.csv to get all the urls
for i in range(1, len(seeds)+1):
    urls_in_report = read_csv_file("report", i)
    
    # go one more layer to get outlinks of urls in report.csv
    # crawler_bot(seeds, max_pages, layer, num_of_report)
    crawler_bot(urls_in_report, 1, 2, i)
    
    for j in range(1, len(urls_in_report)+1):
        urls_in_doc = read_csv_file("doc{}_".format(i), j)