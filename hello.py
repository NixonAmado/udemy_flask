from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/<nombre>')
def index(nombre):
    friends = ['Alice', 'Bob', 'Charlie']

    return render_template('index.html', nombre=nombre, friends=friends )
@app.route('/')
def hello():
    return 'Hello, World!'