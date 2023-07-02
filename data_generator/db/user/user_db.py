import csv

class UserDB : 
    def user_db(self):
        datas =[]    
        #read data from csv file
        with open("csv/user.csv",'r',encoding='utf-8') as file:
            csv_reader=csv.DictReader(file)
            for row in csv_reader:
                clean_row = {key.strip() : value.strip() for key, value in row.items()}
                datas.append(clean_row)  
        return datas

    def read_all(self) : 
        #log
        print('----------------------------db-user : read_all()')
        # select문
        # select * 
        # from users
        return self.user_db()
    
    def read_name_gender(self, name, gender) :
        #log
        print('----------------------------db-user : read_name_gender()')
        datas = self.user_db()
        result = [] 

        # select문
        # select * 
        # from users
        # where name like '%name%' and gender = gender

        for data in datas : 
            if name in data['Name'] and gender == data['Gender'] :
                result.append(data)
        
        return result

    
    def read_name_both_gender(self, name) :
        #log
        print('----------------------------db-user : read_name_both_gender()')
        datas = self.user_db()
        result = [] 

        # select문
        # select * 
        # from users
        # where name like '%name%'

        for data in datas : 
            if name in data['Name'] :
                result.append(data)
        
        return result
        
    def read_id(self, id) :
        #log
        print('----------------------------db-user : read_id()')
        datas = self.user_db()
        result = [] 

        # select문
        # select * 
        # from users
        # where id = id

        for data in datas : 
            if id == data['Id'] :
                result.append(data)
        
        return result