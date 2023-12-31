import csv

class OrderDB : 
    def order_db(self):
        datas =[]    
        #read data from csv file
        with open("db/csv/order.csv",'r',encoding='utf-8') as file:
            csv_reader=csv.DictReader(file)
            for row in csv_reader:
                clean_row = {key.strip() : value.strip() for key, value in row.items()}
                datas.append(clean_row)  
        return datas

    def read_all(self) : 
        #log
        print('----------------------------db-order : read_all()')
        # select문
        # select * 
        # from orders
        return self.order_db()
    
    def read_order_date(self, order_date) : 
        #log
        print('----------------------------db-order : read_order_date()')
        datas = self.order_db()
        result = []
        # select문
        # select * 
        # from orders
        # where order_at = order_date

        for data in datas :
            if order_date == data['OrderAt'][0:10] : 
                result.append(data)

        return result
    
    def read_id(self, id) :
        #log
        print('----------------------------db-order : read_id()')
        datas = self.order_db()
        result = [] 

        # select문
        # select * 
        # from orders
        # where id = id

        for data in datas : 
            if id == data['Id'] :
                result.append(data)
        
        return result