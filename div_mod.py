from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/div_mod', methods=['POST', 'GET'])
def sample_file_upload():
    print(request.method)
    if request.method == 'GET':
        return render_template('div_mod.html', title="Деление")
    elif request.method == 'POST':
        try:
            return str(not int(request.form['number1']) % int(request.form['number2']))
        except ValueError:
            return request.form['number1'] + ' или ' + request.form['number2'] + ' не является корректным целым числом'
        except ZeroDivisionError:
            return 'НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!!!!!!!!!!'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
