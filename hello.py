from glob import escape

from flask import Flask, render_template, url_for

app = Flask(__name__)

#Filtros personalizados
#@app.template_filter('today')
def today(date):
    return date.strftime("%d-%m-%Y")

@app.add_template_global
def repeat(s,n):
    return s * n

app.add_template_filter(today, "today")

from datetime import datetime


@app.route('/')
@app.route('/index/')
def index():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('code', code='print("Hello World")'))

    nombre = "Juan"
    friends = ['Alice', 'Bob', 'Charlie']
    date = datetime.now()

    return render_template(
        'index.html',
        nombre=nombre,
        friends=friends,
        date=date
        )
@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>/<email>')

def hello(name=None, age=None, email=None):
    data = {
        'name': name,
        'age': age,
        'email': email
    }

    return render_template('hello.html', data=data)

@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'