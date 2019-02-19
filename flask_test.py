from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс! Я - Даня"


@app.route('/image_sample')
def image():
    return '''<h1>Цветы</h1>
    <img src="{}" alt="здесь должна была быть картинка, 
    но не нашлась">'''.format(url_for('static', filename='img/test.jpeg'))


@app.route('/bootstrap_sample')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <nav class="navbar navbar-expand-lg navbar-light bg-light">
                    <a class="navbar-brand" href="#">Navbar</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item active">
                                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Features</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Pricing</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link disabled" href="#">Disabled</a>
                            </li>
                        </ul>
                    </div>
                    </nav>
                  </head>
                  <body>
                    <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img class="d-block w-100" src="{url_for('static', filename='img/image2.jpg')}" alt="First slide">
                            </div>
                            <div class="carousel-item">
                                <img class="d-block w-100" src="{url_for('static', filename='img/image.png')}" alt="Second slide">
                            </div>
                            <div class="carousel-item">
                                <img class="d-block w-100" src="https://st7.stpulscen.ru/images/product/063/146/223_big.jpg" alt="Third slide">
                            </div>
                        </div>
                    </div>
                    <center><button type="button" class="btn btn-outline-danger">Danger</button></center>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
