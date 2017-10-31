from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'firstname': 'Brother'}
    return render_template('index.html', title='Home', user=user)
