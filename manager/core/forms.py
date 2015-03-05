from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import Email, InputRequired, EqualTo

class LoginForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class ForgotPasswordForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('E-Mail', validators=[InputRequired(), Email()])

class RegistrationForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    email = StringField('E-Mail', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match!')])
    confirm = PasswordField('Confirm Password')

class NewPasswordForm(Form):
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match!')])
    confirm = PasswordField('Confirm Password')
