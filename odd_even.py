from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/odd_even', methods=['POST', 'GET'])
def sample_file_upload():
    print(request.method)
    if request.method == 'POST':
        return render_template('odd_even_form.html')
    elif request.method == 'GET':
        return render_template('odd_even.html', number=request.number)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
