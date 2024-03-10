from flask import render_template, request, redirect, url_for
from markupsafe import Markup
from app import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/singup")
def  cadastro():
    return render_template('singup.html')

@app.route('/login', methods=['GET','POST'])
def login():  
    if request.method == 'POST' and request.form['username'].split():
        usuario = request.form['username']
        return usuario
    return render_template('login.html')
        #Faço o processamento do formulário aqui
    