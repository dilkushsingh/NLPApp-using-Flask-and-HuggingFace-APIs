from flask import Flask, render_template, request
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
        return 'Registration successfull'
    else:
        return 'Email already exist'


app.run(debug=True)