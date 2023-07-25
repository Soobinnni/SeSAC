from flask import Flask, render_template, request 
from flask import redirect, url_for, session
from flask import flash
import os
from datetime import timedelta

app = Flask(__name__)

app.secret_key = os.urandom(24) # session key가 암호화로 저장되어야 하기 때문
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/<name>")
def user(name="") :
    return render_template('index.html', name = name)

@app.route("/", methods = ["GET", "POST"])
def user2() :
    response = render_template('index3.html')
    if request.method == "POST" :
        name = request.form['name']
        session['name'] = name
        # session.permanent = True 디폴트임.
        flash("룰루랄라")
        flash("롤로")

    return response

@app.route("/name-get")
def user_name_get() :
    name = request.args.get('name')
    return render_template('index2.html', name = name)

@app.route("/jjan")
def user_jjan() :
    return redirect(url_for('user', name='쨘'))

@app.route("/check-session-name")
def check_session_name() :
    if "name" in session :
        return f"{session.get('name')}"
    else :
        return redirect(url_for('user_jjan'))

if __name__ == "__main__" :
    app.run(debug=True)