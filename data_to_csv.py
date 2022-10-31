import json, csv

with open('./data.json', 'r', encoding="UTF-8-sig") as data_json:
    data = json.load(data_json);

keyset = set()
for d in data:
    for k in d.keys():
        keyset.add(k)

keys = list(keyset)

with open('./data.csv' ,'w', newline='', encoding="UTF-8-sig") as data_csv:
    w = csv.DictWriter(data_csv, keys)
    w.writeheader()
    w.writerows(data)
