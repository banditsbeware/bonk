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
  return render_template( 'index.html', 
    posts=BlogPost.query.all(), 
    script=script 
  )

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
  posts = BlogPost.query.all()
  return render_template( 'editor.html', 
  back=True, 
  posts=posts 
)

@routes.route( '/edit/<int:i>' )
@login_required
def edit( i ):
  return render_template( 'editor.html', 
    back=True, 
    editing=BlogPost.query.get( i ), 
    posts=BlogPost.query.all() 
  )

@routes.route( '/save', methods=['POST'] )
@login_required
def save():
  bid = request.form.get( 'bid' )
  txt = request.form.get( 'editor' )
  ttl = request.form.get( 'title' ) or request.form.get( 'prevt' )

  bp = BlogPost.query.get( bid ) if bid else BlogPost()
  bp.title = ttl
  bp.body = txt 
  bp.visible = request.form.get( 'vis' ) is not None
  bp.save()
  return redirect( '/' )

@routes.route( '/post/<int:i>' )
def post( i ):
  p = BlogPost.query.get( i )
  return render_template( 'post.html', 
    back=True, 
    title=p.title, 
    body=p.body 
  )
