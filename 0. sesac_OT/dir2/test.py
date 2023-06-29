import csv

# users = []
# user_info_dic = {
#     "id" : None,
#     "name" : None,
#     "gender" : None,
#     "age" : None,
#     "birthdate" : None,
#     "address": None
# }
# user_info_list = [] 
# with open("user.csv", "r", encoding="utf-8") as file:
#     csv_reader = csv.reader(file)

#     for row in csv_reader:
#         users.append(row)
# print(users)
user_info_dic_list = []
with open('user.csv', 'r', encoding="utf-8") as file:
        csv_data = csv.DictReader(file)
        for data in csv_data:
                user_info_dic_list.append(data) 

print(user_info_dic_list)