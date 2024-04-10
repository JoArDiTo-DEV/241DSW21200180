#COMMIT 3b
#Para este caso, tenemos que importar la libería flask_bootstra con el comando pip

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

#EL SIGUIENTE COMMIT ES EL 3c
