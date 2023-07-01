from db.order.order_db import OrderDB

class OrderService():
    def __init__(self):
        self.order_db = OrderDB()

    def read_all(self):
        #log
        print('----------------------------service : read_all()')
        result = self.order_db.read_all()
        return result
    
    def read_name_gender(self, name, gender):
        #log
        print('----------------------------service : read_name_gender()')

        result = None
        if(gender != 'Both') :
            result = self.order_db.read_name_gender(name, gender)
        else :
            result = self.order_db.read_name_both_gender(name)
            
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service : read_id()')
        result = self.order_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result