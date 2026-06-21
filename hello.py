from glob import escape
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'dev'
)

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

# Crear formulario wtform
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de usuario: ', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email: ', validators=[DataRequired()])
    password = PasswordField('Contraseña: ', validators=[DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Register')

@app.route('/auth/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        return f"Usuario registrado: {username}, Email: {email}, Contraseña: {password}"

    # if request.method == 'POST':
    #     username = request.form['username']
    #     email = request.form['email']
    #     password = request.form['password']

    #     if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
    #         return f"Usuario registrado: {username}, Email: {email}, Contraseña: {password}"
    #     else:
    #         error =  "Error: El nombre de usuario debe tener entre 4 y 25 caracteres, y la contraseña entre 6 y 40 caracteres."
    #         return render_template('auth/register.html', form = form, error = error)


    return render_template('auth/register.html', form = form)