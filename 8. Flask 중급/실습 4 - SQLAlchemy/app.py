from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.instance_path = os.getcwd() # app.instance_path ->애플리케이션의 대체 인스턴스 경로입니다.
                                # 'instance'기본적으로 패키지 또는 모듈 옆의 폴더는 인스턴스 경로로 간주됩니다.
                                # getwd -> 현재 작업 디렉토리를 나타내는 문자열을 반환합니다.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # True면 객체와 db를 동기화하여 commit하지 않아도 됨
app.debug = True
db = SQLAlchemy(app) # db연결

class User(db.Model) :
    __tablename__ = 'user' # 테이블 이름 정의
    # 컬럼 셋업
    id = db.Column(db.String(64), primary_key = True)
    login_id = db.Column(db.String(32))
    login_pwd = db.Column(db.String(32))
    name = db.Column(db.String(16))
    gender = db.Column(db.String(16))
    age = db.Column(db.Integer())
    birthdate = db.Column(db.String(32))
    address = db.Column(db.String(64))

    def __repr__(self) :
        return f'<User> {self.name}, {self.gender}, {self.birthdate}, {self.address}'

    # 관계 셋업
    orderR = db.relationship('Order', backref='user')

class Store(db.Model) :
    __tablename__ = 'store' # 테이블 이름 정의

    id = db.Column(db.String(64), primary_key = True)
    name = db.Column(db.String(16))
    type = db.Column(db.String(16))
    address = db.Column(db.String(64))
    

    def __repr__(self) :
        return f'<Store> {self.name}, {self.type}, {self.address}'
    # 관계 셋업
    orderR = db.relationship('Order', backref='store')

class Order(db.Model) :
    __tablename__ = 'order' # 테이블 이름 정의
    # 컬럼 셋업
    id = db.Column(db.String(64), primary_key = True)
    ordered_at = db.Column(db.String(64))
    user_id = db.Column(db.String(64), db.ForeignKey('user.id'))
    store_id = db.Column(db.String(64), db.ForeignKey('store.id'))

    def __init__(self, orderedat, storeId, userId) :
        self.orderedat = orderedat
        self.storeId = storeId
        self.userId = userId
    # 관계 셋업
    userR = db.relationship('User', backref='order')
    storeR = db.relationship('Store', backref='order')

# 윤수빈이 방문한 상점명들을 출력하시오.

# app route
@app.route("/")
def home() :
    # users = Users.query.all()
    users = User.query.filter_by(name='윤수빈').first()
    order_by_user = users.orderR
    print(order_by_user)
    return "Hello"


if __name__ == "__main__" :
    with app.app_context() :
        db.create_all()
    app.run()