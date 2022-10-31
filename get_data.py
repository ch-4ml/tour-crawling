import requests, json
from bs4 import BeautifulSoup as bs

with open('./ids.json', 'r') as id_json:
    ids = json.load(id_json)["ids"];

data = []
for i in range(0, len(ids)): # len(ids)
    d = {}
    print(ids[i])
    uri = "http://data.visitkorea.or.kr/page/" + str(ids[i])

    page = requests.get(uri)
    soup = bs(page.text, "html.parser")

    elements = soup.select('tbody > tr')
    for idx, element in enumerate(elements):
        k = element.select_one('td').text.strip()
        v = element.select_one('td:nth-of-type(2)').text.strip()
        d[k] = v

    data.append(d)

with open('./data.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(data, ensure_ascii=False))