import csv

l = []
with open("prices.csv", encoding="utf-8") as files:
    reader = csv.DictReader(files, delimiter=";")
    for row in reader:
        for key, val in row.items():
            if key != 'Магазин':
                l.append((row['Магазин'],key,val))  

    a = min(l,key=lambda x: (int(x[2]),x[1],x[0]) )
    print('{}: {}'.format(a[1],a[0]))