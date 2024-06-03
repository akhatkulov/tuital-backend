from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError,DataRequired
from flask_wtf import FlaskForm

class Login(FlaskForm):
    username = StringField("Taxallusingiz",validators=[DataRequired()])
    password = PasswordField("Parolingiz",validators=[DataRequired()])
    submit = SubmitField("Tasdiqlash")

# class Post():
#     name = StringFiel