
from flask import render_template
from app import  db
from sqlalchemy import text
from app.models.tables import User
from app.models.loginform import loginForm
from app.models.singupform import singupForm

def cadastro_():
    form = singupForm()
    if not form.validate_on_submit() and form.errors:
        erro = 'email'
        info = 'Formato de email  inválido!'
        return render_template('singup.html', erro=erro, form=form, info=info)
    if form.validate_on_submit():

        u = User(form.usrname.data, form.password.data, form.name.data, form.email.data)
        
        # Evitar o uso de filter ou filter_by
        sql_query_n = text("SELECT * FROM users WHERE users.usrname =  :uname ")
        sql_query_e = text("SELECT * FROM users WHERE users.email = :email")

        usr_n = db.session.execute(sql_query_n, {"uname": form.usrname.data}).fetchall()
        usr_e = db.session.execute(sql_query_e, {"email": form.email.data   }).fetchall()

        if usr_e:
            erro = 'email'
            info = 'Esse email pertence a outro usuário!'
            return render_template('singup.html',erro=erro, form=form, info=info)
        if usr_n:
            erro = 'username'
            return render_template('singup.html',erro=erro, form=form)

        db.session.add(u)        
        db.session.commit()
        return render_template('login.html', form=loginForm())
    return render_template('singup.html', form=form)

