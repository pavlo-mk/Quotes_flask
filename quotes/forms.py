from wtforms import Form, TextField, BooleanField, RadioField
from wtforms.validators import DataRequired


class LoginForm(Form):
    name = TextField('Name', [DataRequired("Please enter your name.")])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female')])
    remember_me = BooleanField('remember_me', default=False)
