from flask import Flask
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# UPLOAD_FOLDER = "'uploads/'"
UPLOAD_FOLDER = os.path.join(basedir, 'static/uploads/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
SQLALCHEMY_TRACK_MODIFICATIONS = False
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}