from flask import Flask, render_template, request 
from flask import redirect, url_for, session
from flask import flash
import os
from datetime import timedelta

app = Flask(__name__)
app.secret_key = os.urandom(24) # session key가 암호화로 저장되어야 하기 때문


# 미션1. 랜더템플릿 통해서 첫 화면에 login/logout 추가
# 미션2. 로그인 성공 실패 여부를 flash 메시지 통해서 처리
# 미션3. 디자인 적용해서 flash 메시지 색상 다르게 해보기(성공시 초록, 실패시 빨강)

# 가상의 사용자 테이블
users = {
    'user1' : {'password' : 'password123'},
    'user2' : {'password' : 'abc123'}
}
def checkout_auth() :
    login_status = False
    if 'username' in session :
        login_status = True
    return login_status

@app.route("/")
def home() :
    response = None
    login_status = checkout_auth()
    if 'username' in session :
        username = session['username']
        login_status = True
        flash(f'{username}님 안녕하세요.')
    return render_template('home.html', login_status = login_status)

@app.route("/login", methods = ["GET", "POST"])
def login() :
    login_status = checkout_auth()  
    if request.method == "POST" :
        username = request.form['username']
        password = request.form['password']
        login_status = checkout_auth()

        #DB를 통해서 로그인 확인
        if username in users and users[username]['password'] == password :
            session['username'] = username
            login_status = checkout_auth()
            flash({'auth_status' : True, 'msg' : '로그인에 성공하였습니다.'})
        else :
            flash({'auth_status' : False, 'msg' : '이름 또는 패스워드가 잘못 입력되었습니다. 다시 시도해주세요'})

        
        return render_template('login_after.html', login_status = login_status)
        
    return render_template('login.html', login_status = login_status)


@app.route("/logout")
def logout() :
    response = render_template('login.html')
    if checkout_auth() :
        session.pop("username", None)
    return response

if __name__ == "__main__" :
    app.run(debug=True)