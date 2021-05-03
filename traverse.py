import os, sys, csv
from itertools import islice
from datetime import datetime
from parse_page_range import extract_text_from_pdf, get_text_from_file


# enter input dir and num of pages
input_dir = sys.argv[1]
num_pages  = sys.argv[2]
search_term = sys.argv[3]


# traveres directory
file_info = []
for root, dirs, files in os.walk(input_dir):
    for f in files:
        f = f.lower()
        if f.endswith('.pdf'):
            full_path = os.path.join(root, f)
            text = get_text_from_file(full_path, num_pages).lower()

    
            file_info.append({
                'input_dir': input_dir,
                'file_name': f,
                'file_path': full_path,
                'file_text': text
                })


# saves file output
today = datetime.now().strftime('%m-%d-%Y')
filename = f'output_{today}.csv'
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = list(file_info[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in file_info:
        writer.writerow(row)


# searches file output
with open(filename, 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        if search_term in row[3] and row[3] is not None:
            print(row)
