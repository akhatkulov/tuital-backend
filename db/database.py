from flask_sqlalchemy import SQLAlchemy
from conf import app
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.schema import PrimaryKeyConstraint
app.config['SECRET_KEY']="This is secret key, bro!!!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tuit:1945@localhost/tuit'
db = SQLAlchemy(app)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(),unique=True,nullable=False)
    password = db.Column(db.String(),nullable=False)
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    img = db.Column(db.Text(),nullable=False)
    name = db.Column(db.String(),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    view = db.Column(db.Integer,default=0)
    aid = db.Column(db.Integer, db.ForeignKey(User.id))

class News(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    img = db.Column(db.Text(),nullable=False)
    name = db.Column(db.String(),nullable=False)
    body = db.Column(db.Text(),nullable=False)
    view = db.Column(db.Integer,default=0)
    aid = db.Column(db.Integer, db.ForeignKey(User.id))

def get_post_s(i: int):
    x = {}
    for j in range(i-9,i+1):
        y = {}
        d =  Post.query.filter_by(id=int(j)).first()
        if d:
            z = d.img
            y['images']=list(z.split("|"))
            y['name']=d.name
            y['body']=d.body
            y['view']=str(d.view)
        else:
            print(f"Post with id {j} not found.")
        x[str(j)]=y
    return x

def get_news_s(i: int):
    x = {}
    for j in range(i-9,i+1):
        y = {}
        d =  News.query.filter_by(id=int(j)).first()
        if d:
            z = d.img
            y['images']=list(z.split("|"))
            y['name']=d.name
            y['body']=d.body
            y['view']=str(d.view)
        else:
            print(f"News with id {j} not found.")
        x[str(j)]=y
    return x
