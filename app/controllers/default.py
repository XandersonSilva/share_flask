from flask import render_template, request, redirect, url_for
from app import app, db
from sqlalchemy import text
from app.controllers.cadastro import cadastro
from app.models.tables import Upload
from app.models.loginform import loginForm


# app.config['SECRET_KEY'] = 'abcde'

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/singup", methods=['GET', 'POST'])
def cad():
    return cadastro()
    

@app.route('/login', methods=['GET','POST'])
def login():  
    form =   loginForm()
    if form.validate_on_submit():
        usuario = loginForm().usrname.data
        return usuario
    return render_template('login.html',form=form)
        #Faço o processamento do formulário aqui
    