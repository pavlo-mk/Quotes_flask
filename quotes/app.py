from flask import Flask
from flask import render_template, redirect, request, flash

from .forms import LoginForm

quotes = Flask(__name__)


@quotes.route('/')
@quotes.route('/index')
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
    return render_template("index.html", title='Home', user=user, posts=posts)


@quotes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            # ('Login requested for Name="' + form.name.data + '", remember_me=' + str(form.remember_me.data))
            return render_template('login.html', title='Sign In', form=form)
        else:
            return render_template('index.html', title='Home')
                    # redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
