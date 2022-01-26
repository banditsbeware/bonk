from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, SubmitField
from wtforms.validators import InputRequired

class LoginForm( FlaskForm ):
  password  = PasswordField( 'Password', validators=[ InputRequired() ] )
  submit    = SubmitField( 'Log in' )
