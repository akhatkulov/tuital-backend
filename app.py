from flask import render_template,redirect,request,flash,jsonify
from werkzeug.security import check_password_hash,generate_password_hash
from models.forms import Login_form,Sign_Form
from db.database import User,app,db,Post,News,get_news_s,get_post_s
from flask_login import login_user,logout_user,login_required,current_user
from helper.auth import load_user,login_manager
from werkzeug.utils import secure_filename
import os
from conf import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route("/")
def home_page():
    # if current_user.is_authenticated:
        # return redirect("/dashboard")
    # else:
    return render_template("index.html",user=current_user)

@app.route("/signin")
def sign_page():
    form = Sign_Form()
    return render_template("sign.html",form=form)

@app.route("/signing",methods=['post','get'])
def signing():
        with app.app_context():
            form = Sign_Form()
            if form.pwd.data == "mexroj1945":
                print(form.username.data,form.password.data)
                user = User(username=form.username.data,password=generate_password_hash(form.password.data))
                db.session.add(user)
                db.session.commit()
                login_user(user,True)
        return redirect("/")
            
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dash.html")
@app.route("/signup")
def signup():
    form = Login_form()
    return render_template("login.html",form=form)

@app.route("/login",methods=['post','get'])
def login():
    form = Login_form()
    print(form.username.data, form.password.data)
    usr = User.query.filter_by(username=form.username.data).first()
    if usr:
        print(form.username.data, form.password.data)
        if check_password_hash(usr.password, form.password.data):
            login_user(usr)
            return redirect("/dashboard")
        else:
            return "Parol Xato"
    else:
        return "Foydalanuvchi mavjud emas"

@app.route('/news_adder', methods=['POST'])
def news_adder():
    if request.method == 'POST':
        files = request.files.getlist('img[]')
        images_url = ""
        print(files)
        if 'img[]' not in request.files:
            flash('No file part')
            return redirect("/dashboard")
        
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                images_url = images_url + "/static/uploads/"+filename + "|"
            else:
                print("error")

        header = request.form.get('header', '') 
        body = request.form.get('body', '')  

        # Create a new post with form data and image URLs
        post = News(name=header, body=body, img=images_url, aid=current_user.id)
        db.session.add(post)
        db.session.commit()

        return 'Files successfully uploaded and post created'
    else:
        return 'Method not allowed'






@app.route('/poster', methods=['POST'])
def poster():
    if request.method == 'POST':
        files = request.files.getlist('img[]')
        images_url = ""
        print(files)
        if 'img[]' not in request.files:
            flash('No file part')
            return redirect("/dashboard")
        
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                images_url = images_url + "/static/uploads/"+filename + "|"
            else:
                print("error")

        header = request.form.get('header', '') 
        body = request.form.get('body', '')  

        # Create a new post with form data and image URLs
        post = Post(name=header, body=body, img=images_url, aid=current_user.id)
        db.session.add(post)
        db.session.commit()

        return 'Files successfully uploaded and post created'
    else:
        return 'Method not allowed'
    
@app.route("/api/post",methods=['GET'])
def get_post():
    current_page = request.args.get('page')
    x = Post.query.count()
    total_page = x//10
    datas = get_post_s(int(current_page)*10)
    print(datas)
    res = {
        "total_pages":total_page,
        "current_page":current_page,
        "data": datas 
    }
    return res

@app.route("/api/news",methods=['GET'])
def get_news():
    current_page = request.args.get('page')
    x = Post.query.count()
    total_page = x//10
    datas = get_news_s(int(current_page)*10)
    print(datas)
    res = {
        "total_pages":total_page,
        "current_page":current_page,
        "data": datas 
    }
    return res

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/signup")