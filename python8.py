import csv
from datetime import datetime

dict_email = {}
new_email = {}
forma = "%d/%m/%Y %H:%M"
with open("name_log.csv", "r", encoding="utf-8") as csv_files_1:
    read_csv = csv.DictReader(csv_files_1, delimiter=",")
    for row in read_csv:
        dict_email.setdefault(row["email"], []).append(row)

for key, vals in dict_email.items():
    vals = max(vals, key=lambda dates: datetime.strptime(dates["dtime"], forma))
    dict_email[key] = vals
    print(key, " : ", vals)

with open("new_name_log.csv", "w", newline="", encoding="utf-8") as csv_files_2:
    colunce = ["username", "email", "dtime"]
    write_csv = csv.DictWriter(csv_files_2, delimiter=",", fieldnames=colunce)
    write_csv.writeheader()
    for row in sorted(dict_email):
        write_csv.writerow(dict_email[row])
