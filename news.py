from flask import Flask, render_template
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list, title="Новости")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
