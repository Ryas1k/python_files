import csv

with open('wifi.csv','r',encoding='utf-8') as files_csv:
  dict1 = {}
  read_files = csv.DictReader(files_csv,delimiter=';')
  for row in read_files:
    dict1.setdefault(row['district'],[]).append(int(row['number_of_access_points']))
    
  result = {k: sum(v) for k,v in dict1.items()}
  print(result)

  sort1 = sorted(result.items(),key=lambda x: x[0])
  print(sort1)
  sort2 = sorted(sort1,key=lambda x: x[1],reverse=True)
  for k,v in sort2:
    print(k,v,sep=': ')

#2 столб 4