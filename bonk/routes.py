from flask import Flask, Blueprint, render_template, request
import os

bp = Blueprint('bp', __name__, url_prefix='/')

@bp.route('/')
def index():
    # get a list of file names
    mats = os.listdir('bonk/templates/materials')
    # strip ".html"
    mats = [ mat[:-5] for mat in mats ]
    return render_template('index.html', mats=mats)

@bp.route('/mats/<name>')
def mat(name):
    return render_template(f'materials/{name}.html')
