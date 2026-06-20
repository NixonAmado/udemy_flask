from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/<nombre>')
def index(nombre):
    return render_template('index.html', nombre=nombre)
@app.route('/')
def hello():
    return 'Hello, World!'