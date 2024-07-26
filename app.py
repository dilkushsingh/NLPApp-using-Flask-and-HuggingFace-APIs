from flask import Flask, render_template, request, redirect
from mydb import Database
from myapi import API

app = Flask(__name__)
dbo = Database()
apio = API()
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

@app.route('/perform_ner', methods=['post'])
def perform_ner():
    text = request.form.get('text')
    result = apio.ner(text)
    txt = ""
    for i in range(len(result)):
        txt += f"'entity_group':'{result[i]['entity_group']}', 'word':'{result[i]['word']}', 'score':{round(result[i]['score'] * 100, 2)}% \n"
    return render_template('ner.html', result=txt)

@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')

@app.route('/perform_sentiment', methods=['post'])
def perform_sentiment():
    text = request.form.get('text')
    result = apio.sentiment_analysis(text)
    print(result)
    txt = ''
    for i in range(len(result[0])):
        txt += f'{result[0][i]['label']} : {round(result[0][i]['score'] * 100, 2)}%\n'
    return render_template('sentiment.html', result=txt)


@app.route('/emotion')
def emotion():
    return render_template('emotion.html')

@app.route('/perform_emotion', methods=['post'])
def perform_emotion():
    text = request.form.get('text')
    response = apio.emotion(text)
    return render_template('emotion.html', result=response)

app.run(debug=True)