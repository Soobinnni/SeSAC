# from flask import Flask, session
# import os
# from flask_sqlalchemy import SQLAlchemy
# from flask_session import Session
# import json

# app = Flask(__name__)
# app.secret_key = os.urandom(24) # app['SECRET_KEY'] = adskjf 같음

# app.debug = True
# app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite3:///sessions.db'
# db = SQLAlchemy(app)

# app.config['SESSION_TYPE'] = 'sqlalchemy'
# app.config['SESSION_SQLALCHEMY'] = db
# Session(app)

# #세션 저장을 위한 db 저장소 설계(Model)
# class SessionData(db.Model) :
#     id = db.Column(db.String(255), primary_key = True)
#     data = db.Column(db.Text)

# # 세션정보를 db에 저장하는 함수
# def session_store(sid, data):
#     session_data = SessionData.query.get(sid)
#     if not session_data:
#         # sid가 없는 세션 데이터라면 새로 저장
#         session_data = SessionData(id=sid)
#     # 있는 데이터라면 데이터의 
#     session_data.data = json.dump(data)
#     db.session.add(session_data)
#     db.session.commit()

# def get_session_data(sid):
#     session_data = SessionData.query.get(sid)
#     if session_data:
#         return json.loads(session_data.data)
    
#     return {}



# @app.route("/")
# def index() :
#     session['username'] = 'user'
#     session['data'] = 'data123'

#     # 숫자 데이터 저장
#     session['count'] = 42
#     # 리스트 데이터 저장
#     session['my_list'] = [1,2,3,4,5]

#     # 세션 데이터 저장
#     session_store(session.sid, dict(session)) # 식별 id, session에 저장된 값의 dictionary
#     return "Hello"

# @app.route("/get_session")
# def get_session_data_route():
#     username = session.get('username')
#     data = session.get('data')

#     # 저장된 데이터 가져오기
#     stored_session_data = get_session_data(session.sid)
#     print(stored_session_data)
#     # 세션 데이터를 화면에 출력 가능한 형태로 변경
#     stored_session_str = json.dumps(stored_session_data, indent=4)

#     return f"username={username}이고, data={data}입니다.\nmy-data={stored_session_str}"

# if __name__ == "__main__" :
#     with app.app_context():
#         db.create_all()

#     app.run()