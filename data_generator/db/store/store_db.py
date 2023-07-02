import csv

class StoreDB : 
    def store_db(self):
        datas =[]    
        #read data from csv file
        with open("csv/store.csv",'r',encoding='utf-8') as file:
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