with open('files_csv\products.csv', encoding='utf-8') as file:
    data = file.read()
    for line in data.splitlines():
        print(line.split(','))