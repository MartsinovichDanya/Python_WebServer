import requests
x = []
all_zp = 0
all_n = 0
for i in range(10):
    # запрос
    url = 'https://api.hh.ru/vacancies'
    par = {'text': 'Python Junior', 'area': '113', 'per_page': '1', 'page': i}
    r = requests.get(url, params=par)
    print(r)
    e = r.json()
    print(e)
