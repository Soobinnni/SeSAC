from service.mk_uuid import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService, DML

import sqlite3

class UserService(ExecuteSQLService):
# =========================================================CREATE=========================================================
    def create(self, user) :
        #log
        print('----------------------------service-user : create()')

        #domain
        user = user

        # uuid init, object property -> tuple
        id = user.id = mk_uuid()
        user_tuple = self.properties_to_tuple(user)

        #execute sql
        sql = "INSERT INTO user(id, name, gender, age, birthdate, address) VALUES (?, ?, ?, ?, ?, ?)"
        args = user_tuple
        self.execute_sql(DML.INSERT, sql, args)

        #return
        return id
    
# =========================================================READ=========================================================
    def read_all(self):
        #log
        print('----------------------------service-user : read_all()')
        
        #execute sql
        sql = "SELECT * FROM user"
        result = self.execute_sql(DML.SELECT, sql)
        return result
    
    def read_name_gender(self, name, gender):
        #log
        print('----------------------------service-user : read_name_gender()')
        
        #execute sql
        result = None
        sql = "SELECT * FROM user WHERE name = ?"
        if(gender != 'Both') :
            sql += "AND gender = ?"
            args = (name, gender)
        else :
            args = (name,)
        
        result = self.execute_sql(DML.SELECT, sql, args)
        
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-user : read_id()')

        #execute sql
        sql = "SELECT * FROM user WHERE id = ?"
        args = (id,)
        result = self.execute_sql(DML.SELECTONE, sql, args)
        return result
    
# =========================================================etc-=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())