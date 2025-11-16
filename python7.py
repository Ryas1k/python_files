import csv

dict_male = {}
dict_female = {}
with open("titanic.csv", "r", encoding="utf-8") as file_csv:
    read_file = csv.DictReader(file_csv, delimiter=";")
    for row in read_file:
        if row["survived"] == "1" and float(row["age"]) < 18:
                dict_male.setdefault(row["sex"], []).append(row["name"])
for key in sorted(dict_male,reverse=True):
     print(*dict_male[key],sep='\n')  

