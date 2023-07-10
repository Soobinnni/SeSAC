import sqlite3

class ExecuteSQLService:
    def get_conn_cursor(self) :
        conn = sqlite3.connect("db/crm.db")
        cursor = conn.cursor()

        return conn, cursor

    def execute_select(self, sql, args = None):
        # get conn, cursor
        conn, cursor = self.get_conn_cursor()
        # get dic-resultset
        result = self.fetchall_as_dict(cursor, sql, args)
        # conncect close
        conn.close()

        return result

    def execute_select_one(self, sql, args):
        # get conn, cursor
        conn, cursor = self.get_conn_cursor()
        # get dic-resultset
        result = self.fetchone_as_dict(cursor, sql, args)
        # conncect close
        conn.close()
        return result

    def execute_insert(self, sql, args) :
        # get conn, cursor
        conn, cursor = self.get_conn_cursor()
        #execute insert
        cursor.execute( sql, args )
        conn.commit()
        conn.close()

    def execute_update(self, conn, cursor, sql, args):
        # get conn, cursor
        conn, cursor = self.get_conn_cursor()
        cursor.execute( sql,  args)
        conn.commit()
        conn.close()

    def execute_delete(self, conn, cursor, sql, args):
        # get conn, cursor
        conn, cursor = self.get_conn_cursor()
        cursor.execute( sql,  args)
        conn.commit()
        conn.close()

    def fetchall_as_dict(self, cursor, sql, args):
        if args != None:
            cursor.execute(sql, args)
        else : 
            cursor.execute(sql)
        columns = [column[0] for column in cursor.description]  #[컬럼명, ...]
        rows = cursor.fetchall()
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))  # key : value = column : column value
        return result

    def fetchone_as_dict(self, cursor, sql, args):
        cursor.execute(sql, args)

        columns = [column[0] for column in cursor.description]  #[컬럼명, ...]
        row = cursor.fetchone()
        result = {}
        for i, r in enumerate(row):
            result[columns[i]] = r  # key : value = column : column value
        return result