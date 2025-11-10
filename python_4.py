import csv

with open('deniro.csv','r',encoding='utf-8') as csv_files:
  readered = csv.reader(csv_files,delimiter=',') 
  l = list(readered) 
  sort_stolb = int(input())-1
  l.sort(key=lambda x: int(x[sort_stolb]) if x[sort_stolb].isdigit() else x[sort_stolb])
  print(l)  
  for i in l:
    print(','.join(i))
