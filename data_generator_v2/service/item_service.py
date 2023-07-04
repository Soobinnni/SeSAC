from db.item_db import ItemDB
from service.mk_uuid import mk_uuid

class ItemService():
    def __init__(self):
        self.item_db = ItemDB()

    def read_all(self):
        #log
        print('----------------------------service-item : read_all()')
        result = self.item_db.read_all()
        return result
    
    def read_name(self, name):
        #log
        print('----------------------------service-item : read_name()')
        result = self.item_db.read_name(name.strip())
        return result
    
    def read_name_price(self, name, price):
        #log
        print('----------------------------service-item : read_name_price()')
        result = self.item_db.read_name_price(name.strip(), price.strip())
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service : read_id()')
        result = self.item_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result
    
    def create(self, item) :
        #log
        print('----------------------------service-item : create()')

        #domain
        item = item

        #property
        uuid = mk_uuid()
        name = item.name
        type_ = item.type_
        unit_price = item.unit_price

        #list
        item_list = [uuid, name, type_, unit_price]

        #db
        self.item_db.create(item_list)