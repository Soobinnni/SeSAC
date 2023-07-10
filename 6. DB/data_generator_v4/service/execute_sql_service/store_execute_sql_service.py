from service.mk_uuid import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService

class StoreExecuteSQLService(ExecuteSQLService):
    def read_all(self):
        #log
        print('----------------------------service-store : read_all()')
        # result = db.store_db.read_all()
        # return result
    
    def read_address(self, address):
        #log
        print('----------------------------service-store : read_address()')
        # result = db.store_db.read_address(address.strip())
        # return result
    
    def read_name(self, name):
        #log
        print('----------------------------service-store : read_name()')
        # result = db.store_db.read_name(name.strip())
        # return result
    
    def read_name_address(self, name, address):
        #log
        print('----------------------------service-store : read_name_address()')
        # result = self.store_db.read_name_address(name.strip(), address.strip())
        # return result
    
    def read_id(self, id):
        #log
        print('----------------------------service-store : read_id()')
        # result = self.store_db.read_id(id)[0]
        # # select 1개이므로 인덱스 번호 0의 dic을 반환
        # return result
    
    def create(self, store) :
        #log
        print('----------------------------service-store : create()')

        #domain
        store = store

        #property
        uuid = mk_uuid()
        name = store.name
        type_ = store.type_
        address = store.address

        #list
        store_list = [uuid, name, type_, address]

        #db
        # self.store_db.create(store_list)

        # return uuid