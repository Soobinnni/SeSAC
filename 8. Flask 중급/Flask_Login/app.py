from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
from werkzeug.security import generate_password_hash, check_password_hash

"""
LoginManager: 로그인 관리를 담당하는 클래스로, Flask 애플리케이션에서 로그인 기능을 초기화하고 관리하는 역할을 합니다.

UserMixin: UserMixin 클래스는 Flask-Login이 기본적으로 사용하는 사용자 모델 클래스를 정의하기 위해 사용됩니다. 
            이 클래스를 사용하여 사용자 모델 클래스에 필요한 메서드들을 간단하게 추가할 수 있습니다.

login_user: 로그인 처리를 위해 사용되는 함수로, 인증이 성공적으로 완료된 사용자를 로그인 상태로 만듭니다. 
            이 함수를 호출하면 세션에 사용자 정보가 저장되어 사용자를 인증된 상태로 유지할 수 있습니다.

login_required: 데코레이터로, 특정 뷰 함수를 보호하는 데 사용됩니다. 이 데코레이터가 적용된 뷰 함수는 로그인된 사용자만 접근할 수 있으며, 
                로그인되지 않은 사용자는 로그인 페이지로 리디렉션됩니다.

logout_user: 로그아웃 처리를 위해 사용되는 함수로, 현재 로그인된 사용자를 로그아웃 상태로 만듭니다. 
                세션에서 사용자 정보를 삭제하여 인증을 끝내는 역할을 합니다.

current_user: 현재 로그인된 사용자를 나타내는 객체입니다. 로그인되지 않은 경우 AnonymousUserMixin 객체가 반환됩니다. 
                이를 통해 로그인된 사용자의 정보를 뷰 함수에서 간단하게 접근할 수 있습니다.
"""

app = Flask(__name__)

# config
app.secret_key = os.urandom(24)  # 보안을 위한 시크릿 키 설정
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db 생성
db = SQLAlchemy(app)

# Flask-Login 초기화
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# 사용자 정보 모델
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column("password", db.String(80), nullable = False)
    email = db.Column(db.String(80))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __init__(self, username, email) :
        self.username = username
        self.email = email


# 로그인 뷰
@app.route('/login', methods=['GET', 'POST'])
def login(): # 사용자 인증 처리
    # 로그인 기능 구현
    # 1. Form으로부터 id/pw를 받아온다
    # 2. DB로부터 쿼리해서 id/pw가 맞는지 확인한다.
    # 3. 성공했으면? 로그인 정보를 저장하고 로그인 한 페이지로 이동한다.
    #    실패라면 오류를 알려준다.
    if request.method == 'POST' :
        username = request.form.get('username')
        password = request.form.get('password')
        # user = User.query.filter_by(username=username).first() : filter_by는 인자가 하나만 되므로 filter함수를 사용한다
        user = User.query.filter(User.username == username).first()
        if user and user.check_password(password) : 
            login_user(user)
            flash('로그인에 성공하셨습니다!')
            return redirect(url_for('home'))
        else :
            flash('로그인에 실패하셨습니다!')
            return redirect(url_for('login'))
        
    return render_template('login.html')

# 로그아웃 뷰
@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# 로그인 필요한 보호된 뷰
@app.route('/profile-edit', methods = ['GET', 'POST'])
@login_required
def profile_edit():
    if request.method == 'POST' :
        new_password = request.form['new_password']
        user = User.query.filter_by(username=current_user.username).first()
        if user:
            user.set_password(new_password)
            db.session.commit()

            return redirect(url_for("home"))

    return render_template("profile_edit.html")

    # 미션1 프로필 수정 기능 구현
    # 1. 폼을 통해서 수정할 정보를 가져온다(password를 받아온다)
    # 2. 저장할 장소(즉 현재 사용자)를 가져온다. (current_user를 통해서 접근 가능)
    # 3. 받아온 정보를 DB에 저장한다.


# 홈 페이지
@app.route('/')
def home():
    return render_template('home.html')

# 신규 사용자 생성
@app.route("/register", methods = ['GET', 'POST'])
def register():
    # 회원 가입 폼을 만든다.
    # 회원 가입 정보를 받아온다(id/pw)
    # DB에 저장한다.
    if request.method == "POST" :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        existing_user = User.query.filter(User.username==username).first()
        if existing_user :
            return '이미 존재하는 회원입니다.'

        create_user(username, password, email)
        flash('회원가입이 완료되었습니다. 로그인해주세요!')
        return render_template("home.html")
    return render_template("register.html")

# 로그아웃 뷰
@app.route('/withdraw', methods=['POST'])
@login_required
def withdraw():
    user = User.query.filter_by(username=current_user.username).first()
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('home'))

# 사용자 목록 조회
@app.route("/users")
@login_required
def users():
    users = User.query.all()
    return render_template("users.html", users = users)


# 사용자 로드 함수
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) #input값은 String이기 때문에 int로 변환

# 사용자 생성 함수 (새로운 사용자 생성)
def create_user(username, password, email):
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # 데이터베이스 테이블 생성

    app.run() 