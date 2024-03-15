from flask import render_template, redirect, url_for
from app import app, db
from app.controllers.cadastro import cadastro_
from app.controllers.login import login_
from app.models.tables import Upload
from app.models.tables import User
from app.models.loginform import loginForm 
from flask_login import logout_user, current_user


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signup", methods=['GET', 'POST'])
def cad():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return cadastro_()
    

@app.route('/login', methods=['GET','POST'])
def login():  
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return login_(loginForm())
        
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


