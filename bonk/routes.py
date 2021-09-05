from flask import Flask, Blueprint, render_template, request
import os

# router = Flask(__name__, template_folder='scaff')

router = Blueprint('router', __name__, url_prefix='/')

@router.route('/')
def index():
    # get a list of file names
    mats = os.listdir('bonk/scaff/mats')
    # strip ".html"
    mats = [ mat[:-5] for mat in mats ]
    return render_template('index.html', mats=mats)

@router.route('/mats/<name>')
def mat(name):
    return render_template(f'mats/{name}.html')
