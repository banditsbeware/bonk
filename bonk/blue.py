from flask import Flask, Blueprint, render_template, request, make_response
from random import choice
from .blog import read
import os


bp = Blueprint('bp', __name__, url_prefix='/')


@bp.route('/')
def index():

  script = f'static/animations/{choice(os.listdir("bonk/static/animations"))}'

  return render_template('index.html', dr=read(), script=script)


@bp.route('/mat/<int:i>')
def mat(i):

  dr = read()
  
  return render_template(f'materials/{i}.html', title=dr[i]['title'], back=True)
