from flask import render_template,redirect
from werkzeug.security import check_password_hash,generate_password_hash
from models.forms import Login_form,Sign_Form
from db.database import User,app,db
from flask_login import login_user,logout_user,login_required,current_user
from helper.auth import load_user,login_manager
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

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/signup")