from datetime import datetime
from bonk import db
from sqlalchemy.sql import func, expression

class BlogPost( db.Model ):
  __tablename__ = 'blogpost'
  __table_args__ = { 'extend_existing': True }
  bid       = db.Column( db.Integer, autoincrement=True, primary_key=True )
  title     = db.Column( db.String(80), nullable=False )
  body      = db.Column( db.Text, nullable=False )
  visible   = db.Column( db.Boolean, server_default=expression.false() )
  published = db.Column( db.DateTime, nullable=False, server_default=func.now() )
  updated   = db.Column( db.DateTime, onupdate=func.now() )

  def save( self ):
    db.session.add( self )
    db.session.commit()

  def __repr__( self ):
    return f'[Post: "{ self.title }"]'


from flask_login import UserMixin
class User( UserMixin, db.Model ):
  __tablename__ = 'user'
  __table_args__ = { 'extend_existing': True }
  uid           = db.Column( 'id', db.Integer, autoincrement=True, primary_key=True )
  email         = db.Column( db.String( 40 ) )
  password      = db.Column( db.String( 20 ) )
  name          = db.Column( db.String( 20 ) )
  authenticated = db.Column( db.Boolean, default=False )

  def get_id( self ):
    return self.uid

  def __repr__( self ):
    return f'[User: "{ self.email }"]'


from bonk import login_manager
@login_manager.user_loader
def load_user( uid ):
  return User.query.get( int( uid ) )