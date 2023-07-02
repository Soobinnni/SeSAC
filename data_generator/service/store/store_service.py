from db.store.store_db import StoreDB

class StoreService():
    def __init__(self):
        self.store_db = StoreDB()

    def read_all(self):
        #log
        print('----------------------------service-store : read_all()')
        result = self.store_db.read_all()
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-store : read_id()')
        result = self.store_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result