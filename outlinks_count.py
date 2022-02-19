import csv


def write_links_count(link, count, filename):
    with open(filename, 'a', newline='') as report:
        _writer = csv.writer(report)
        _writer.writerow([link, count])


def clear_report_file(filename):
    with open(filename, 'w', newline='') as report:
        report.close()
