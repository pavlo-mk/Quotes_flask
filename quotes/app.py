from flask import Flask, render_template, redirect, request, flash, url_for

from .forms import LoginForm

quotes = Flask(__name__)
quotes.secret_key = 'lhflkk24hflk24jlfk4l25kfh4lk5hfl45khf'


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
        if form.validate() == True:
            # flash('All fields are required.')
            # ('Login requested for Name="' + form.name.data + '", remember_me=' + str(form.remember_me.data))
            return render_template('success.html')

        else:
            return render_template('login.html', title='Sign In', form=form)
                    # redirect('/index')
    elif request.method == 'GET':
        return render_template('login.html', form=form)



# @quotes.route('/success')
# def success():
#     return 'welcome name'
#
# @quotes.route('/login-test', methods=['POST', 'GET'])
# def login_test():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success', name=user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success', name=user))


if __name__ == '__main__':
   quotes.run(debug = True)