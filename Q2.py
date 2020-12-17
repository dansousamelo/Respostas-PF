import csv

# Lendo csv
with open('./file.csv') as file_csv:
    reader = csv.reader(file_csv, delimiter=';')

    data = list(reader)
    res_list = []

    keys = [x for x in data[0]]

    print(keys)

    res = []

    # Colocando campos em dicionários
    for row in data[1::]:
        res_dict = dict()
        for i in range(len(keys)):
            res_dict[keys[i]] = row[i]
        
        res.append(res_dict)
    
    # Ordenando valores
    res = sorted(res, key = lambda i: i['nome'])
    print(res)