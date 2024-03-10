from flask import render_template, request, redirect, url_for
from app import app
from app.models.loginform import loginForm
from markupsafe import Markup
#app.config['SECRET_KEY'] = 'abcde'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/singup")
def  cadastro():
    return render_template('singup.html')

@app.route('/login', methods=['GET','POST'])
def login():  
    form =   loginForm()
    if form.validate_on_submit():
        usuario = loginForm().username.data
        return usuario
    return render_template('login.html',form=form)
        #Faço o processamento do formulário aqui
    