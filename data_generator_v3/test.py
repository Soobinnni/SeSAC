import csv
# #TODO : app완성 시 삭제 시킬 파일(test.py)

# page_list = list(range(1, 14))

# print(page_list)


# result = [page_list [i:(i+3)] for i in range(0, len(page_list), 3)]
# print(result)

# datas =[]    
# #read data from csv file
# with open("db/csv/item.csv",'r',encoding='utf-8') as file:
#     csv_reader=csv.DictReader(file)
#     for row in csv_reader:
#         clean_row = {key.strip() : value.strip() for key, value in row.items()}
#         datas.append(clean_row)  
# a= []
# for data in datas :
#     a.append(data['Type'])

# print(set(a))

# result = []
# # select문
# # select * 
# # from orders
# # where order_at = order_date

# for data in datas :
#     print(len(data['OrderAt'][0:10]) )

# a = 'ㅁㅇㅇ '
# print(a.strip())
# from db.mk_uuid import mk_uuid
# datas = [ 'Nikhil', 'COE', '2', '9.0']
# print(datas)
# # data = []
# # # data.append(','.join(datas))
# # print(type(data))
# # print(data)
# with open("test.csv",'a',encoding='utf-8', newline='') as file:
#         csv_writer=csv.writer(file)
#         csv_writer.writerow(datas)

# from service.user_service import UserService
# from domain.user import User

# user_service = UserService()
# user = User('김수빈', 'Female', 26, '1998-06-17', '서울시 강동구 올림픽로')
# user_service.create(user)

a = "asdf"
b = "1.5"
c = 1

print(int(b))

if type(b) != type(c) : 
    print('타입이 다릅니다.')