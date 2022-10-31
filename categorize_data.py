import json
from unicodedata import category

with open('./data.json', 'r', encoding="UTF-8-sig") as data_json:
    data = json.load(data_json);

category_set = set()
for d in data:    
    if "rdf:type" in d:
        category = d['rdf:type']
        # if "\n" in category:
            # category = category[1:category.index("\n")]
        category_set.add(category)

categories = list(category_set)
c = []
for idx, category in enumerate(categories):
    c.append({"idx" : idx, "category": category})

with open('./categories.json' ,'w', encoding="UTF-8-sig") as file:
    file.write(json.dumps(c, ensure_ascii=False))
