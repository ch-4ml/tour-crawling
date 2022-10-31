import requests, json
from bs4 import BeautifulSoup as bs

ids = [];

for i in range(0, 1000):  # 1000
    print(i)
    start = 1000 * i

    uri = "http://data.visitkorea.or.kr/sparql?query=PREFIX+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E%0D%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+dc%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Felements%2F1.1%2F%3E%0D%0APREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E%0D%0APREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0APREFIX+vi%3A+%3Chttp%3A%2F%2Fwww.saltlux.com%2Ftransformer%2Fviews%23%3E%0D%0APREFIX+kto%3A+%3Chttp%3A%2F%2Fdata.visitkorea.or.kr%2Fontology%2F%3E%0D%0APREFIX+ktop%3A+%3Chttp%3A%2F%2Fdata.visitkorea.or.kr%2Fproperty%2F%3E%0D%0APREFIX+ids%3A+%3Chttp%3A%2F%2Fdata.visitkorea.or.kr%2Fresource%2F%3E%0D%0APREFIX+wgs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%3E%0D%0APREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E%0D%0APREFIX+geo%3A+%3Chttp%3A%2F%2Fwww.saltlux.com%2Fgeo%2Fproperty%23%3E%0D%0APREFIX+pf%3A+%3Chttp%3A%2F%2Fwww.saltlux.com%2FDARQ%2Fproperty%23%3E+%0D%0A%0D%0ASELECT+*+%0D%0AWHERE+%7B%0D%0A+%3Fresource+a+kto%3APlace+%3B%0D%0A++++++rdfs%3Alabel+%3Fname+.%0D%0A+%0D%0A%7D+ORDER+BY+%3Fresource%0D%0Alimit+1000+offset+" + str(start) + "%0D%0A++%09%0D%0A++%09%09%09%09%0D%0A%09%09%09&format=html&timeout_second=30&btn_execute="

    page = requests.get(uri)
    soup = bs(page.text, "html.parser")

    elements = soup.select('tr > td > a')
    for idx, element in enumerate(elements):
        text = element.text
        text = text[text.rindex("/") + 1:]
        ids.append(text)

file_path = "./ids.json"
data = {}
data["ids"] = ids

with open(file_path, 'w') as outfile:
    json.dump(data, outfile)


