import csv

class OrderItemDB : 
    def order_item_db(self):
        datas =[]    
        #read data from csv file
        with open("csv/orderitem.csv",'r',encoding='utf-8') as file:
            csv_reader=csv.DictReader(file)
            for row in csv_reader:
                clean_row = {key.strip() : value.strip() for key, value in row.items()}
                datas.append(clean_row)  
        return datas

    def read_all(self) : 
        #log
        print('----------------------------db-order_item : read_all()')
        # select문
        # select * 
        # from orderitems
        return self.order_item_db()
    
    # def read_name_gender(self, name, gender) :
    #     #log
    #     print('----------------------------db-order_item : read_name_gender()')
    #     datas = self.order_item_db()
    #     result = [] 

    #     # select문
    #     # select * 
    #     # from orderitems
    #     # where name like '%name%' and gender = gender

    #     for data in datas : 
    #         if name in data['Name'] and gender == data['Gender'] :
    #             result.append(data)
        
    #     return result

    
    # def read_name_both_gender(self, name) :
    #     #log
    #     print('----------------------------db-order_item : read_name_both_gender()')
    #     datas = self.order_item_db()
    #     result = [] 

    #     # select문
    #     # select * 
    #     # from orderitems
    #     # where name like '%name%'

    #     for data in datas : 
    #         if name in data['Name'] :
    #             result.append(data)
        
    #     return result
        
    def read_id(self, id) :
        #log
        print('----------------------------db-order_item : read_id()')
        datas = self.order_item_db()
        result = [] 

        # select문
        # select * 
        # from orderitems
        # where id = id

        for data in datas : 
            if id == data['Id'] :
                result.append(data)
        
        return result