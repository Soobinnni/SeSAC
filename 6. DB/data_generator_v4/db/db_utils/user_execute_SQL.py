import csv

from db.db_utils.db_utils import DbUtils

class UserExecuteSQL : 
    def __init__(self) :
        self.db_path = "db/crm.db"
        self.db_utils = DbUtils(self.db_path)

    # ================================================READ================================================

    def read (self, sql, args= None): 
        #log
        print('----------------------------UserExecuteSQL : read()')

        result = self.db_utils.execute_select(sql, args)    
        return result
    
    def read_by_id(self, id) :
        #log
        print('----------------------------UserExecuteSQL : read_by_id()')

        result =  self.db_utils.execute_select_one(sql, id)
        
        return result
    # ================================================CREATE================================================
    def create(self, user_tuple) :
        #log
        print('----------------------------db-user : create()')
        self.add_user_db(user_tuple)