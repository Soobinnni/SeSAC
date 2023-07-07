import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('user.db')
cursor = conn.cursor()

# 사용자 테이블 생성
# cursor.execute('''CREATE TABLE IF NOT EXISTS users
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 age INTEGER,
#                 gender TEXT)''')

# # 몇 명의 사용자 추가
# users = [
#     ('John Doe', 25, 'Male'),
#     ('Jane Smith', 30, 'Female'),
#     ('Michael Johnson', 35, 'Male'),
#     ('Emily Davis', 28, 'Female'),
#     ('David Lee', 32, 'Male'),
#     ('Emma Wilson', 27, 'Female'),
#     ('Daniel Brown', 31, 'Male'),
#     ('Olivia Taylor', 29, 'Female'),
#     ('Sophia Anderson', 33, 'Female'),
#     ('Matthew Martin', 26, 'Male')
# ]

# cursor.executemany('INSERT INTO users (name, age, gender) VALUES (?, ?, ?)', users)

# 변경사항 저장
# conn.commit()

# =============미션==================
def fetchall_as_dict(cursor, sql):
    cursor.execute(sql)

    columns = [column[0] for column in cursor.description]  
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(dict(zip(columns, row))) 
    return result

def print_select_result(select_result_list):
    for i, dic in enumerate(select_result_list) :
        print(f"\n{i+1}번째 레코드")
        for column, record in dic.items() :
            print(f"{column}은 {record}입니다.")

# #미션 1 : 성별이 여자인 사람 출력
# sql_1 = "SELECT * FROM users WHERE gender = 'Female'"
# dic_list_1 = fetchall_as_dict(cursor, sql_1)
# print('\n미션 1 : 성별이 여자인 사람 출력')
# print_select_result(dic_list_1)

# #미션 2 : 나이가 30살 이상인 사람 출력
# sql_2 = "SELECT * FROM users WHERE age >= 30"
# dic_list_2 = fetchall_as_dict(cursor, sql_2)
# print('\n미션 2 : 나이가 30살 이상인 사람 출력')
# print_select_result(dic_list_2)

# #미션 3 : 나이 25이상 30세 이하 출력
# sql_3 = "SELECT * FROM users WHERE age >= 25 AND age <= 30"
# dic_list_3 = fetchall_as_dict(cursor, sql_3)
# print('\n미션 3 : 나이 25이상 30세 이하 출력')
# print_select_result(dic_list_3)

# #미션 4 : 성별로 그룹핑(남/여 각각) 몇명인지 출력
# sql_4 = "SELECT count(*) as count FROM users GROUP BY gender"
# dic_list_4 = fetchall_as_dict(cursor, sql_4)
# print('\n미션 4 : 성별로 그룹핑(남/여 각각) 몇명인지 출력')
# print_select_result(dic_list_4)

#미션 5 : John Doe의 나이를 25살에서 26으로 UPDATE
sql_5 = "UPDATE users SET age = 26 WHERE name = 'John Doe'"
cursor.execute(sql_5)
conn.commit

#결과 출력해보기
sql_5_1 = "SELECT * FROM users WHERE name = 'John Doe'"
dic_lis_5_1 = fetchall_as_dict(cursor, sql_5_1)
print_select_result(dic_lis_5_1)


#미션 6 : Emily Davis 사용자 삭제
sql_6 = "DELETE FROM users WHERE name = 'Emily Davis'"
cursor.execute(sql_6)
conn.commit

#결과 출력해보기
sql_6_1 = "SELECT * FROM users WHERE name = 'Emily Davis'"
result = cursor.execute(sql_6_1).fetchall()
if not result :
    print('조회결과 없음')


#close
conn.close()
