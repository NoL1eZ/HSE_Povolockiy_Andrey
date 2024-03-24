import json
import pprint
import csv

with open('traders.txt', 'r') as file:
    traders_inn = file.read()
    # print(traders_inn)


with open('traders.json', 'r') as file:
    data = json.load(file)

traders = []

for trader in data:
        if trader['inn'] in traders_inn:
            traders.append(trader)

with open('traders.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['INN', 'OGRN', 'ADDRESS'])
    for i in traders:
        writer.writerow([i['inn'], i['ogrn'], i['address']])
