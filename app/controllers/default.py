from flask import render_template, request, redirect, url_for
from app import app, db
from sqlalchemy import text
from app.models.tables import User
from app.models.tables import Upload
from app.models.loginform import loginForm
from app.models.singupform import singupForm

# app.config['SECRET_KEY'] = 'abcde'

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/singup", methods=['GET', 'POST'])

def cadastro():
    form = singupForm()

    if form.validate_on_submit():
        u = User(form.username.data, form.password.data, form.name.data, form.email.data)
        
        # Evitar o uso de filter ou filter_by
        sql_query_n = text("SELECT * FROM users WHERE users.usrname =  :uname ")
        sql_query_e = text("SELECT * FROM users WHERE users.email = :email")

        usr_n = db.session.execute(sql_query_n, {"uname": form.username.data}).fetchall()
        usr_e = db.session.execute(sql_query_e, {"email": form.email.data   }).fetchall()

        if usr_e:
            erro = 'usr_e'
            return render_template('singup.html',erro=erro, form=form)
        if usr_n:
            erro = 'usr_n'
            return render_template('singup.html',erro=erro, form=form)

        db.session.add(u)        
        db.session.commit()
        return render_template('login.html',form=loginForm())


    return render_template('singup.html', form=form, erro='')

@app.route('/login', methods=['GET','POST'])
def login():  
    form =   loginForm()
    if form.validate_on_submit():
        usuario = loginForm().username.data
        return usuario
    return render_template('login.html',form=form)
        #Faço o processamento do formulário aqui
    