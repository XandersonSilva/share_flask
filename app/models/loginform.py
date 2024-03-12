from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
    usrname = StringField("usrname",validators=[DataRequired()])
    password = PasswordField("password",validators=[DataRequired()])


