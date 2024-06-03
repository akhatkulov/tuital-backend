from flask_sqlalchemy import SQLAlchemy
from conf import app
from flask_login import UserMixin
from sqlalchemy.schema import PrimaryKeyConstraint
app.config['SECRET_KEY']="This is secret key, bro!!!"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1945@localhost/dd'
db = SQLAlchemy(app)

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(),unique=True,nullable=False)
    password = db.Column(db.String(),nullable=False)
# class Post(db.Model):
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     img = db.Column(db.Text(),nullable=False)
#     name = db.Column(db.String(),nullable=False)
#     body = db.Column(db.Text(),nullable=False)
#     view = db.Column(db.Integer,default=0)
#     aid = db.Column(db.Integer, db.ForeignKey(User.id))

# class News(db.Model):
#     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     img = db.Column(db.Text(),nullable=False)
#     name = db.Column(db.String(),nullable=False)
#     body = db.Column(db.Text(),nullable=False)
#     view = db.Column(db.Integer,default=0)
#     aid = db.Column(db.Integer, db.ForeignKey(User.id))

