import csv

class ItemDB : 
    def item_db(self):
        datas =[]    
        #read data from csv file
        with open("db/csv/item.csv",'r',encoding='utf-8') as file:
            csv_reader=csv.DictReader(file)
            for row in csv_reader:
                clean_row = {key.strip() : value.strip() for key, value in row.items()}
                datas.append(clean_row)  
        return datas

    def read_all(self) : 
        #log
        print('----------------------------db-item : read_all()')
        # select문
        # select * 
        # from itmes
        return self.item_db()

    def read_name(self, name) : 
        #log
        print('----------------------------db-item : read_name()')
        datas = self.item_db()
        result = [] 
        # select문
        # select * 
        # from itmes
        # where name like %name%
        for data in datas : 
            if name.lower() in data['Name'].lower() :
                result.append(data)
        return result

    def read_price(self, price) : 
        #log
        print('----------------------------db-item : read_price()')
        datas = self.item_db()
        result = [] 
        # select문
        # select * 
        # from itmes
        # where price = price
        for data in datas : 
            if price == int(data['UnitPrice']) :
                result.append(data)
        return result

    def read_name_price(self, name, price) : 
        #log
        print('----------------------------db-item : read_name_price()')
        datas = self.item_db()
        result = [] 
        # select문
        # select * 
        # from itmes
        # where name like %name% and price = price
        for data in datas : 
            if name.lower() in data['Name'].lower() and price == int(data['UnitPrice']) :
                result.append(data)
        return result
        
    def read_id(self, id) :
        #log
        print('----------------------------db-item : read_id()')
        datas = self.item_db()
        result = [] 

        # select문
        # select * 
        # from items
        # where id = id

        for data in datas : 
            if id == data['Id'] :
                result.append(data)
        
        return result
    # -----------------------------------------CREATE-----------------------------------------------------
    def add_item_db(self, data):
        #create data to csv file
        with open("db/csv/item.csv",'a',encoding='utf-8', newline='') as file:
            csv_writer=csv.writer(file)
            csv_writer.writerow(data)

    def create(self, item_list) :
        #log
        print('----------------------------db-item : create()')
        self.add_item_db(item_list)