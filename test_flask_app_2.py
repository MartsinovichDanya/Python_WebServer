from flask_restful import reqparse, abort, Api, Resource
import sqlite3
from flask import Flask, jsonify
import os.path
import hashlib
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


class DB:
    def __init__(self):
        conn = sqlite3.connect('news.db', check_same_thread=False)
        self.conn = conn

    def get_connection(self):
        return self.conn

    def __del__(self):
        self.conn.close()


class UserModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             user_name VARCHAR(50),
                             password_hash VARCHAR(128),
                             admin BOOL
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, user_name, password):
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO users 
                          (user_name, password_hash, admin) 
                          VALUES (?,?,?)''',
                       (user_name, hashlib.md5(bytes(password, encoding='utf8')).hexdigest(), False))
        cursor.close()
        self.connection.commit()

    def get(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (str(user_id)))
        row = cursor.fetchone()
        return row

    def get_all(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return rows

    def exists(self, user_name, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = ? AND password_hash = ?",
                       (user_name, hashlib.md5(bytes(password, encoding='utf8')).hexdigest()))
        row = cursor.fetchone()
        return (True, row[0], row[-1]) if row else (False,)


class NewsModel:
    def __init__(self, connection):
        self.connection = connection

    def init_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS news 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             title VARCHAR(100),
                             content VARCHAR(1000),
                             date VARCHAR(12),
                             user_id INTEGER
                             )''')
        cursor.close()
        self.connection.commit()

    def insert(self, title, content, user_id):
        date = datetime.today()
        cursor = self.connection.cursor()
        cursor.execute('''INSERT INTO news 
                          (title, content, date, user_id) 
                          VALUES (?,?,?,?)''', (title, content, date.strftime("%d.%m.%Y"), str(user_id)))
        cursor.close()
        self.connection.commit()

    def get(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM news WHERE id = ?", (str(news_id)))
        row = cursor.fetchone()
        return row

    def get_all(self, user_id=None):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT * FROM news WHERE user_id = ?",
                           (str(user_id)))
        else:
            cursor.execute("SELECT * FROM news")
        rows = cursor.fetchall()
        return rows

    def delete(self, news_id):
        cursor = self.connection.cursor()
        cursor.execute('''DELETE FROM news WHERE id = ?''', (str(news_id)))
        cursor.close()
        self.connection.commit()

    def get_count(self, user_id=None):
        cursor = self.connection.cursor()
        if user_id:
            cursor.execute("SELECT COUNT(*) FROM news WHERE user_id = ?",
                           (str(user_id)))
        else:
            cursor.execute("SELECT COUNT(*) FROM news")
        rows = cursor.fetchone()
        return rows[0]


def abort_if_news_not_found(news_id):
    if not NewsModel(db.get_connection()).get(news_id):
        abort(404, message="News {} not found".format(news_id))


class News(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        news = NewsModel(db.get_connection()).get(news_id)
        return jsonify({'news': news})

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        NewsModel(db.get_connection()).delete(news_id)
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('content', required=True)
parser.add_argument('user_id', required=True, type=int)


class NewsList(Resource):
    def get(self):
        news = NewsModel(db.get_connection()).get_all()
        return jsonify({'news': news})

    def post(self):
        args = parser.parse_args()
        news = NewsModel(db.get_connection())
        news.insert(args['title'], args['content'], args['user_id'])
        return jsonify({'success': 'OK'})


api.add_resource(NewsList, '/news') # для списка объектов
api.add_resource(News, '/news/<int:news_id>') # для одного объекта

if __name__ == '__main__':
    if not os.path.exists('news.db'):
        db = DB()
        um = UserModel(db.get_connection())
        um.init_table()
        um.insert('test1', 'test1')
        um.insert('test2', 'test2')
        nm = NewsModel(db.get_connection())
        nm.init_table()
    else:
        db = DB()
    app.run(port=8080, host='127.0.0.1')

