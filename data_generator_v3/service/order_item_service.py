from db.order_item_db import OrderItemDB

class OrderItemService():
    def __init__(self):
        self.order_item_db = OrderItemDB()

    def read_all(self):
        #log
        print('----------------------------service-order_item : read_all()')
        result = self.order_item_db.read_all()
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-order_item : read_id()')
        result = self.order_item_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result