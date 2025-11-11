import csv

list_email = {}
with open("popular domains\data.csv", "r", encoding="utf-8") as csv_files:
    read_files = csv.reader(csv_files, delimiter=",")
    for r in read_files:
        if r[-1].find("@") != -1:
            b = r[-1][r[-1].find("@") + 1 :]
            list_email[b] = list_email.get(b, 0) + 1

sort_email = sorted(list_email.items(),key=lambda item: [item[1], item[0]])     

with open('popular domains\domain_usage.csv','w',encoding='utf-8', newline='') as csv_write:
    columns = ['domain', 'count']
    write_files = csv.writer(csv_write,delimiter=',')
    write_files.writerow(columns)
    for s0,s1 in sort_email:
        write_files.writerow([s0,s1])