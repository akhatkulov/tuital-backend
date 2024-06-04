from werkzeug import *
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Length, ValidationError,DataRequired
from flask_wtf import FlaskForm

class Login_form(FlaskForm):
    username = StringField("Taxallusingiz",validators=[DataRequired()])
    password = PasswordField("Parolingiz",validators=[DataRequired()])
    submit = SubmitField("Tasdiqlash")

class Sign_Form(FlaskForm):
    username = StringField("Taxallusingiz",validators=[DataRequired()])
    password = PasswordField("Parolingiz",validators=[DataRequired()])
    pwd = StringField("Adminlik uchun",validators=[DataRequired()])
    submit = SubmitField("Tasdiqlash")
