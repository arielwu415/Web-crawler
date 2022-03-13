def make_text_files_no_commas():
    with open('./wordcount1.csv', 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()
        with open('./nocommaswordcount1.txt', 'w', encoding='utf-8') as txt_file:
            for line in lines:
                txt_file.write(line.replace(',', ' '))

    with open('./wordcount2.csv', 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()
        with open('./nocommaswordcount2.txt', 'w', encoding='utf-8') as txt_file:
            for line in lines:
                txt_file.write(line.replace(',', ' '))

    with open('./wordcount3.csv', 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()
        with open('./nocommaswordcount3.txt', 'w', encoding='utf-8') as txt_file:
            for line in lines:
                txt_file.write(line.replace(',', ' '))