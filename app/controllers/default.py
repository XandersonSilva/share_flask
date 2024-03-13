from flask import render_template, request, redirect, url_for
from app import app, db
from sqlalchemy import text
from app.controllers.cadastro import cadastro_
from app.models.tables import Upload
from app.models.tables import User
from app.models.loginform import loginForm 
from flask_login import login_user, logout_user


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/signup", methods=['GET', 'POST'])
def cad():
    return cadastro_()
    

@app.route('/login', methods=['GET','POST'])
def login():  

    form =   loginForm()
    if form.validate_on_submit():
        usuario = loginForm().usrname.data

        user = User.query.filter_by(usrname=usuario).first() or User.query.filter_by(email=usuario).one()
       

        if not user.verify_password(form.password.data):
            return redirect(url_for('login')) 

        login_user(user)
        return render_template('index.html')

    return render_template('login.html',form=form)
        
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


