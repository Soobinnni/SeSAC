from db.store.store_db import StoreDB

class StoreService():
    def __init__(self):
        self.store_db = StoreDB()

    def read_all(self):
        #log
        print('----------------------------service-store : read_all()')
        result = self.store_db.read_all()
        return result
    
    # def read_name_gender(self, name, gender):
    #     #log
    #     print('----------------------------service-store : read_name_gender()')

    #     result = None
    #     if(gender != 'Both') :
    #         result = self.user_db.read_name_gender(name, gender)
    #     else :
    #         result = self.user_db.read_name_both_gender(name)
            
    #     return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-store : read_id()')
        result = self.store_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result