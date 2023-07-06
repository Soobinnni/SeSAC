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

    def execute_select(self, sql, args=None):
        result = None
        if args is None:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        else:
            self.cursor.execute(sql, args)
            result = self.cursor.fetchall()
        return result

    def execute_update(self, sql, args=None):
        if args is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, args)

    def execute_delete(self, sql, args=None):
        if args is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, args)

    def execute_insert(self, sql, args):
        self.cursor.execute(sql, args)
