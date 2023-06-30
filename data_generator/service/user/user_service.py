from db.user.user_db import UserDB

class UserService():
    def __init__(self):
        self.user_db = UserDB()

    def read_all(self):
        #log
        print('----------------------------service : read_all()')
        return self.user_db.read_all()
    
    def read_name_gender(self, name, gender):
        #log
        print('----------------------------service : read_name_gender()')
        return self.user_db.read_name_gender(name, gender)
    
    def read_id(self, id):
        #log
        print('----------------------------service : read_id()')
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return self.user_db.read_id(id)[0]