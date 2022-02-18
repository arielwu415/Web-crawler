import csv


def write_links_count(link, count, filename):
    with open(filename, 'w', newline='') as report:
        _writer = csv.writer(report)
        _writer.writerow([link, count])
