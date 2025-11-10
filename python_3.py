import csv

new_dict = {}
with open("salary_data.csv", "r", encoding="utf-8") as csv_files:
    ritel = csv.DictReader(csv_files, delimiter=";")
    for row in ritel:
        new_dict.setdefault(row["company_name"], []).append(int(row["salary"]))
print(len(new_dict))

for key in new_dict:
    new_dict[key] = sum(new_dict[key]) / len(new_dict[key])

print(*sorted(new_dict,key=new_dict.get),sep='\n')
