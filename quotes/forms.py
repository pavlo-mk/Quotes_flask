from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, length, ValidationError


class LoginForm(FlaskForm):
    name = TextField(u'Name', [DataRequired("Please enter your name."), length(max=20)])
    gender = SelectField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    remember_me = BooleanField('remember_me', default=False)
