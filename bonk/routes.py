import os
from flask import Blueprint, render_template, redirect, flash, request
from random import choice

from flask_login import current_user, login_required, login_user, logout_user

from bonk import db, config
from bonk.models import BlogPost, User
from bonk.forms import LoginForm

routes = Blueprint( 'routes', __name__ )

@routes.route('/', methods=[ 'GET', 'POST' ] )
def index():

  script = f'static/animations/{choice(os.listdir("bonk/static/animations"))}'
  posts = BlogPost.query.all()

  return render_template( 'index.html', posts=posts, script=script )


@routes.route( '/login', methods=[ 'GET', 'POST' ] )
def login():
  form = LoginForm()
  if form.validate_on_submit():
    ME = User.query.get( 1 )
    if form.password.data == ME.password:
      login_user( ME )
      return redirect( request.args.get( 'next' ) or 'editor.html' )
  return render_template( 'login.html', form=form )

@routes.route( '/logout' )
@login_required
def logout():
  logout_user()
  return redirect( '/' )


@routes.route('/editor')
@login_required
def editor():
  return render_template( f'editor.html', back=True )