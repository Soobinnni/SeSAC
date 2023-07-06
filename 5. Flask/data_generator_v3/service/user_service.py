from db.user_db import UserDB
from domain.user import User
from service.mk_uuid import mk_uuid

class UserService():
    def __init__(self):
        self.user_db = UserDB()

    def read_all(self):
        #log
        print('----------------------------service-user : read_all()')
        result = self.user_db.read_all()
        return result
    
    def read_name_gender(self, name, gender):
        #log
        print('----------------------------service-user : read_name_gender()')

        result = None
        if(gender != 'Both') :
            result = self.user_db.read_name_gender(name.strip(), gender)
        else :
            result = self.user_db.read_name_both_gender(name.strip())
            
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-user : read_id()')
        result = self.user_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result
    
    def create(self, user) :
        #log
        print('----------------------------service-user : create()')

        #domain
        user = user

        #property
        uuid = mk_uuid()
        name = user.name
        gender = user.gender
        age = user.age
        birthdate = user.birthdate
        address = user.address

        #list
        user_list = [uuid, name, gender, age, birthdate, address]

        #db
        self.user_db.create(user_list)

        #return으로 id값을 줌 -> view에서 user/detail페이지의 인자로 넘길 수 있게.
        return uuid