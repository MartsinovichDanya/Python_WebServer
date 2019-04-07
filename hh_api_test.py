import requests
import json
x = []
all_zp = 0
all_n = 0
for i in range(1):
    url = 'https://api.hh.ru/vacancies'
    url2 = 'https://api.hh.ru/areas'
    par = {'text': 'Python Junior', 'area': '1', 'per_page': '5', 'page': i}
    r = requests.get(url, params=par)
    if i == 0:
        print(r.json())
    r2 = requests.get(url2)
    e = r2.json()[0]['areas']
    regioni = {}
    for el in e:
        if len(el['areas']) == 0:
            regioni[el['name'].lower()] = el['id']
        for el2 in el['areas']:
            regioni[el2['name'].lower()] = el2['id']
    with open("regioni.json", "w", encoding='utf8') as write_file:
        json.dump(regioni, write_file)
    with open("regioni.json", "r") as read_file:
        data = json.load(read_file)
    print(data)
    print(data['Москва'.lower()])
    # for name, id in regioni.items():
    #     print(name, id)
