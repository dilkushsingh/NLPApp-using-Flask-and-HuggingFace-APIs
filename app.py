from flask import Flask, render_template, request, redirect
from mydb import Database

app = Flask(__name__)
dbo = Database()
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.add_user(name, email, password)
    if response:
        return render_template('login.html', message='Registration Successfull. Kindly Login.', color=1)
    else:
        return render_template('registration.html', message='Email Already exist.')

@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    response = dbo.search_user(email, password)
    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect Email/Password', color=0)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/sentiment')
def sentiment():
    return 'sentimen'

@app.route('/emotion')
def emotion():
    return 'emotion'
app.run(debug=True)