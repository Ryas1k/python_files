import csv

with open('files_csv\sales\sales.csv','r',encoding='utf-8') as csv_files:
    ritel = csv.DictReader(csv_files, delimiter=';')
    selector = filter(lambda item: int(item['old_price']) > int(item['new_price']),ritel) 
    print(*[k['name'] for k in selector],sep='\n')
    