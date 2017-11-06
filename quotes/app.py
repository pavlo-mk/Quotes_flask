from flask import Flask, render_template, redirect, request, flash, url_for
from flask_wtf.csrf import CSRFProtect
from wtforms import Form, BooleanField, StringField, SubmitField, PasswordField
from wtforms.validators import length, DataRequired, InputRequired, ValidationError


# App config
DEBUG = True
quotes = Flask(__name__)
csrf = CSRFProtect(quotes)
quotes.secret_key = '14hj3'


@quotes.route('/')
def index():
    user = {'nickname': 'Man'}
    posts = [
        {
            'author': {'nickname': 'Dr. Seuss'},
            'body': 'Dont cry because its over, smile because it happened.'
        },
        {
            'author': {'nickname': 'Oscar Wilde'},
            'body': 'Be yourself; everyone else is already taken.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


class LoginForm(Form):
    login = StringField('Login', validators=[InputRequired(), length(min=3, max=30)])
    password = PasswordField('Password', validators=[DataRequired(message='Passwords must match')])
    remember_me = BooleanField('Remember me', default=False)
    submit = SubmitField('Login')


@quotes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate() is False:
            flash('All fields are required.')
            return render_template('login.html', title='Sign In', form=form)
        else:
            flash('Hello ' + form.login.data + '!')
            return redirect('/')
    else:
        return render_template('login.html', title='Sign In', form=form)


@quotes.route('/test')
def test():
    return render_template('test.html')
