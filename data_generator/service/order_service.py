from db.order_db import OrderDB

class OrderService():
    def __init__(self):
        self.order_db = OrderDB()

    def read_all(self):
        #log
        print('----------------------------service-order : read_all()')
        result = self.order_db.read_all()
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-order : read_id()')
        result = self.order_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result