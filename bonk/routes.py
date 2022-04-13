import os
from flask import Blueprint, render_template, redirect, request, send_from_directory
from random import choice

from flask_login import current_user, login_required, login_user, logout_user

from bonk.models import BlogPost, User
from bonk.forms import LoginForm

routes = Blueprint( 'routes', __name__ )

@routes.route('/', methods=[ 'GET', 'POST' ] )
def index():
  script = f'static/animations/{choice(os.listdir("bonk/static/animations"))}'
  return render_template( 'index.html', 
    posts=BlogPost.query.all(), 
    # script=script 
  )

@routes.route('/journal')
def journal():
  f = choice( os.listdir( 'bonk/static/journal' ) )
  return render_template( 'journal.html', page=f )

@routes.route( '/favicon.ico' )
def favicon():
  return send_from_directory( os.path.join( app.root_path, 'static' ), 'ntern.png' )

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

@routes.route( '/editor' )
@login_required
def editor():
  posts = BlogPost.query.all()
  return render_template( 'editor.html', 
  back=True, 
  posts=posts 
)
