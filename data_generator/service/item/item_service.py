from db.item.item_db import ItemDB

class ItemService():
    def __init__(self):
        self.item_db = ItemDB()

    def read_all(self):
        #log
        print('----------------------------service-item : read_all()')
        result = self.item_db.read_all()
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service : read_id()')
        result = self.item_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result