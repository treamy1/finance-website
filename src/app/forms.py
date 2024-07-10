

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, PasswordField, TextAreaField, SubmitField, validators, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
#from wtforms_sqlalchemy.fields import QuerySelectField

class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')