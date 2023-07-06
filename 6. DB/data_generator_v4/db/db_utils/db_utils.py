import sqlite3

class DbUtils:
    def __init__(self, path):
        self.conn = self.connect_to_database(path)
        self.cursor = self.conn.cursor()

    def connect_to_database(self, path):
        connection = sqlite3.connect(path)
        return connection
    
    def commit(self) :
        self.conn.commit()

    def conn_close(self) :
        self.conn.close()

    def execute_select(self, sql, args):
        result = self.fetchall_as_dict(self.cursor, sql, args)
        return result
    
    def execute_select_one(self, sql, args):
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        return result

    # TODO : 무조건 commit하도록 종료되는 함수가 신경쓰임! 바람직한 종료를 생각해보기!
    def execute_update(self, sql, args=None):
        if args is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, args)
        self.commit()
        self.conn_close

    def execute_delete(self, sql, args=None):
        if args is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, args)
        self.commit()
        self.conn_close

    def execute_insert(self, sql, args):
        self.cursor.execute(sql, args)
        self.commit()
        self.conn_close


    # TODO : service가 아니라 db_utils모듈에 있는 것이 적합한지 모르겠음(db_utils는 crud 등 db를 활용하는 것에만 그쳐야한다고 생각)
    #        지금은 dic형태로 반환하지만, 튜플을 요소로 하는 list를 반환해도 되도록 고쳐보기..
    def fetchall_as_dict(self, cursor, sql, args=None):
        if args is not None:
            cursor.execute(sql, args)
        else : 
            cursor.execute(sql)

        columns = [column[0] for column in cursor.description]  # 컬럼명 리스트 추출
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))  # 컬럼명과 값의 쌍을 딕셔너리로 변환하여 리스트에 추가
        return result