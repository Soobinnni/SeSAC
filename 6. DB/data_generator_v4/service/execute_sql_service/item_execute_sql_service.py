from service.mk_uuid_service import mk_uuid
from service.execute_sql_service.execute_sql_service import ExecuteSQLService

class ItemExecuteSQLService(ExecuteSQLService):
# =========================================================CREATE=========================================================
    def create(self, item) :
        #log
        print('----------------------------service-item : create()')

        #domain
        item = item

        # uuid init, object property -> tuple
        uuid = mk_uuid()
        item_tuple = self.properties_to_tuple(item)
        
        #execute sql
        sql = "INSERT INTO item(id, name, type, unit_price) VALUES (?, ?, ?, ?)"
        args = item_tuple
        self.execute_insert(sql, args)
        
        #return
        return uuid
# =========================================================READ=========================================================
    def read_all(self):
        #log
        print('----------------------------service-item : read_all()')
        result = db.item_db.read_all(self.conn, self.cursor)
        return result
    
    def read_name(self, name):
        #log
        print('----------------------------service-item : read_name()')
        result = db.item_db.read_name(name.strip())
        return result
    
    def read_price(self, price):
        #log
        print('----------------------------service-item : read_price()')
        result = db.item_db.read_price(price)
        return result
    
    def read_name_price(self, name, price):
        #log
        print('----------------------------service-item : read_name_price()')
        result = db.item_db.read_name_price(name.strip(), price)
        return result
    
    def read_id(self, id):
        #log
        print('----------------------------service : read_id()')
        result = db.item_db.read_id(id)[0]
        # select 1개이므로 인덱스 번호 0의 dic을 반환
        return result
    
# =========================================================etc-=========================================================
    # object property -> tuple
    def properties_to_tuple(self, obj) :
        return tuple(obj.__dict__.values())