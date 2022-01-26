import os
from flask import Blueprint, render_template, redirect, flash, request
from random import choice

from flask_login import current_user, login_required, login_user

from bonk import db, config
from bonk.models import BlogPost
from bonk.forms import LoginForm

routes = Blueprint( 'routes', __name__ )

@routes.route( '/login', methods=[ 'GET', 'POST' ] )
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.password.data == config.password:
      user = User.query.get( 1 )
      login_user( user )
      return redirect( request.args.get( 'next' ) or 'editor.html' )
  return render_template( 'login.html', form=form )

@routes.route('/', methods=[ 'GET', 'POST' ] )
def index():

  script = f'static/animations/{choice(os.listdir("bonk/static/animations"))}'
  posts = BlogPost.query.all()

  return render_template('index.html', posts=posts, script=script)


@routes.route('/b/<int:i>')
@login_required
def mat(i):

  dr = read()
  
  return render_template(f'materials/{i}.html', title=dr[i]['title'], back=True)