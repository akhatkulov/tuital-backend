from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_login import UserMixin
app.config['SECRET_KEY']="This is secret key, bro!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1945@localhost/db'
db = SQLAlchemy(app)

class User(db.Model,UserMixin):
    id = db.Column(db.Intiger,primary_key=True,autoincrement=True)
    username = db.Column(db.String(),primary_key=True,nullable=False)
    password = db.Column(db.String(),nullable=False)
class Post(db.Model):
    id = db.Column(db.Intiger,primary_key=True,autoincrement=True)
    img = db.Column(db.Text(),nullable=False)
    name = db.Column(db.String(),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    view = db.Column(db.Intiger,default=0)
    aid = db.Column(db.Integer, db.ForeignKey(User.id))

class News(db.Model):
    id = db.Column(db.Intiger,primary_key=True,autoincrement=True)
    img = db.Column(db.Text(),nullable=False)
    name = db.Column(db.String(),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    view = db.Column(db.Intiger,default=0)
    aid = db.Column(db.Integer, db.ForeignKey(User.id))

