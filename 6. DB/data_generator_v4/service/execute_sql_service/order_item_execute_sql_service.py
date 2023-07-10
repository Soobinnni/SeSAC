from service.execute_sql_service.execute_sql_service import ExecuteSQLService

class OrderItemExecuteSQLService(ExecuteSQLService):
    def read_all(self):
        #log
        print('----------------------------service-order_item : read_all()')
        # result = db.order_item_db.read_all()
        # return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-order_item : read_id()')
        # result = db.order_item_db.read_id(id)[0]
        # # select 1개이므로 인덱스 번호 0의 dic을 반환
        # return result