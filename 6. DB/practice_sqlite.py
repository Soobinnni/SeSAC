import sqlite3


# c.execute("""
#         CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, password TEXT)
# """) 
# conn.commit()
# users = [('kim', '123'),('lee', '234'),('choi', '345'),('jung', '456'),('park', '567')]
# for user in users :
#     c.execute("""
#             INSERT INTO user (user_name, password) VALUES(?, ?)
#     """, user) 
#     conn.commit()
# c.execute("""
#         SELECT * FROM user
# """) 
# result = c.fetchall()
# print(result)

# columns = [column[0] for column in c.description]

# print(columns)

# #db사용이 끝났을 때 변경사항들을 최종 기록하기 위해서
# conn.commit()
# conn.close()
#==============================================================
#미션 로그인 코드를 구현한다.
#==============================================================
# conn = sqlite3.connect("practice.db")#DB에 접속

# # cursor : 현재 내 명령어를 받는 위치
# c = conn.cursor()
# input_user_id = input('아이디를 입력하세요.\n>>>')
# input_password =  input('비밀번호를 입력하세요.\n>>>\n')

# sql = "SELECT * FROM user WHERE user_name = ? AND password = ?"
# input_ = (input_user_id, input_password)

# result = c.execute(sql, input_).fetchall()

# if(result) :
#     print('로그인 성공!')
# else : 
#     print('로그인 실패!')
# input_ = (input_user_id, input_password)
# sql = "INSERT INTO user(user_name, password) VALUES(?, ?)"

# result = c.execute(sql, input_)

# if(result) :
#     print('로그인 성공!')
# else : 
#     print('로그인 실패!')

#==============================================================
#미션 로그인 코드를 구현한다.
#==============================================================
import hashlib  

# ========================================함수
def input_for_sign_up() :
    print('회원가입을 시작합니다.')
    input_user_id = input('아이디를 입력하세요.\n>>>')
    input_password =  input('비밀번호를 입력하세요.\n>>>\n')

    # 아이디 중복검사 함수
    is_it_duplicate = check_id_duplication(input_user_id)
    if is_it_duplicate :
        hashed_password = get_hashed_password(input_password)
        return (input_user_id, hashed_password)
    else : 
        print('중복된 아이디입니다.')
        return None
def input_for_login() : 
    print('로그인을 시작합니다.')
    input_user_id = input('아이디를 입력하세요.\n>>>')
    input_password =  input('비밀번호를 입력하세요.\n>>>\n')

    hashed_password = get_hashed_password(input_password)
    return (input_user_id, hashed_password)

def check_id_duplication(id_) :
    is_it_duplicate = False
    select_sql_st = "SELECT * FROM users WHERE user_name = ?"
    args_select = (id_,)

    result = execute_select_sql(select_sql_st, args_select)

    if(len(result) ==0) :
        is_it_duplicate = True

    return is_it_duplicate

def get_hashed_password(password):
    m = hashlib.sha256()
    m.update(password.encode('utf-8'))
    hashed_passsword = m.hexdigest()
    return hashed_passsword

def db_utils() :
    conn = sqlite3.connect("practice.db")
    c = conn.cursor()

    return conn, c

def execute_insert_sql(update_sql_st, args) :
    conn , c = db_utils()
    c.execute(update_sql_st, args)
    conn.commit()

def execute_select_sql(select_sql_st, args = None) :
    _ , c = db_utils()
    result = []
    result = c.execute(select_sql_st, args).fetchall()
    return result
# ========================================실행
# 회원가입 : 미션1. 사용자 콘솔로부터 username/password를 받아서 동작 함수 구현
# args_sign_up = input_for_sign_up()
# if args_sign_up :
#     update_sql_st = "INSERT INTO users(user_name, password) VALUES (?, ?)"
#     execute_insert_sql(update_sql_st, args_sign_up)
#결과 조회
# select_sql_st = "SELECT * FROM users WHERE user_name = ? AND password = ?"
# result = execute_select_sql(select_sql_st, args)
# print(result)

#로그인
args_login = input_for_login()
select_sql_st = "SELECT * FROM users WHERE user_name = ? AND password = ?"
result = execute_select_sql(select_sql_st, args_login) 
if result :
    print('로그인 성공!')
else : 
    print('로그인 실패!')