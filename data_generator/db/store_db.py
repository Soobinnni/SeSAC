import csv

class StoreDB : 
    def store_db(self):
        datas =[]    
        #read data from csv file
        with open("db/csv/store.csv",'r',encoding='utf-8') as file:
            csv_reader=csv.DictReader(file)
            for row in csv_reader:
                clean_row = {key.strip() : value.strip() for key, value in row.items()}
                datas.append(clean_row)  
        return datas

    def read_all(self) : 
        #log
        print('----------------------------db-store : read_all()')
        # select문
        # select * 
        # from stores
        return self.store_db()

    def read_address(self, address) : 
        #log
        print('----------------------------db-store : read_address()')
        datas = self.store_db()
        result = [] 
        # select문
        # select * 
        # from stores
        # where address like '%address%'
        for data in datas : 
            if address in data['Address'] :
                result.append(data)
        
        return result

    def read_name(self, name) : 
        #log
        print('----------------------------db-store : read_name()')
        datas = self.store_db()
        result = [] 
        # select문
        # select * 
        # from stores
        # where name like '%name%'
        for data in datas : 
            if name in data['Name'] :
                result.append(data)
        
        return result

    def read_name_address(self, name, address) : 
        #log
        print('----------------------------db-store : read_name_address()')
        datas = self.store_db()
        result = [] 
        # select문
        # select * 
        # from stores
        # where address like '%address%' and name like '%name%'
        for data in datas : 
            if name in data['Name'] and address in data['Address'] :
                result.append(data)
        return result
    
    def read_id(self, id) :
        #log
        print('----------------------------db-store : read_id()')
        datas = self.store_db()
        result = [] 

        # select문
        # select * 
        # from stores
        # where id = id

        for data in datas : 
            if id == data['Id'] :
                result.append(data)
        
        return result