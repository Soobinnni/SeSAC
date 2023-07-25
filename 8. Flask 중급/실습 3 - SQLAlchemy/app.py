from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # True면 객체와 db를 동기화하여 commit하지 않아도 됨
db = SQLAlchemy(app) # db연결

class Users(db.Model) :
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, password, email) :
        self.name = name
        self.password = password
        self.email = email

@app.route("/")
def home() :
    return render_template("home.html")

@app.route("/view")
def view() :
    return render_template("view.html", users = Users.query.all())

@app.route("/login", methods = ["GET", "POST"])
def login() :
    if request.method == "POST" :
        username = request.form.get('username')
        password = request.form.get('password')
        email = f"{username}@aaa.com"
        found_user = Users.query.filter_by(name=username).first()
        if found_user :
            flash("Login Success")
        else :
            user = Users(username, password, email)
            db.session.add(user)
            db.session.commit()
            session['username'] = username
            flash("User Created", "info")

        session['username'] = username
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/delete', methods = ['POST', 'GET'])
def delete() :
    user = session['username']
    if request.method == "POST" :
        action = request.form['action']
        if action == 'DELETE' :
            Users.query.filter_by(name = user).delete()
            db.session.commit()
            return redirect(url_for("logout"))
        
    return render_template("delete.html")
        
@app.route("/logout")
def logout() :
    session.pop('username', None)
    return render_template("home.html")

if __name__ == "__main__" :
    with app.app_context() :
        db.create_all()
    app.run(debug=True)