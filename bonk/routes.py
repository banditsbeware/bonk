from flask import Flask, Blueprint, render_template, request
# import database as db
import os

# router = Flask(__name__, template_folder='scaff')

router = Blueprint('router', __name__, url_prefix='/')

@router.route('/')
def index():
    mats = os.listdir('bonk/scaff/mats')
    return render_template('index.html', mats=mats)

@router.route('/mats/<name>')
def mat(name):
    return render_template(f'mats/{name}')

