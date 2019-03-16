from requests import get, post, delete

print(get('http://localhost:8080/news').json())
print(get('http://localhost:8080/news/1').json())
print(get('http://localhost:8080/news/8').json())


print(post('http://localhost:8080/news').json())
print(post('http://localhost:8080/news',
           json={'title': 'Заголовок'}).json())
print(post('http://localhost:8080/news',
           json={'title': 'Заголовок',
                 'content': 'Текст новости',
                 'user_id': 1}).json())


print(delete('http://localhost:8080/news/8').json())
print(delete('http://localhost:8080/news/3').json())
