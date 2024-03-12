from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email


class  singupForm(FlaskForm):

    name         = StringField("name",validators=[DataRequired()])
    username     = StringField("username",validators=[DataRequired()])
    email        = StringField("email",validators=[DataRequired(), Email() ])
    password     = PasswordField("password",validators=[DataRequired()])
    cfm_password = PasswordField("cfm_password",validators=[DataRequired()])


