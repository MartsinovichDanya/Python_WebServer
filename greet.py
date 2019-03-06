from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/greeting_form', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return render_template('greet.html', title="Приветствие")
    elif request.method == 'POST':
        return 'Привет, ' + request.form['name']


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
