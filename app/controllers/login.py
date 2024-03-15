from flask import render_template, redirect, url_for
from app.models.tables import User
from app.models.loginform import loginForm 
from flask_login import login_user

def login_(form):
    if form.validate_on_submit():
        usuario = loginForm().usrname.data

        user = User.query.filter_by(usrname=usuario).first() or User.query.filter_by(email=usuario).one()

        if not user.verify_password(form.password.data):
            return redirect(url_for('login')) 

        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html',form=form)