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
# user_info_dic_list = []
# with open('user.csv', 'r', encoding="utf-8") as file:
#         csv_data = csv.DictReader(file)
#         for data in csv_data:
#                 user_info_dic_list.append(data) 

# print(user_info_dic_list)



datas = [{'Id': '0a497257-2b1a-4836-940f-7b95db952e61', 'Name': '강준영', 'Gender': 'Male', 'Age': '28', 'Birthdate': '1994-09-08', 'Address': '대구 강서구 59길 66'}, {'Id': '3e00736a-5978-48ee-9aa9-366b0c4ed0b8', 'Name': '장승현', 'Gender': 'Female', 'Age': '43', 'Birthdate': '1979-11-05', 'Address': '서울 강남구 88길 78'}, {'Id': '7b5dda41-7547-4660-ab66-3ad52f739fff', 'Name': '조하은', 'Gender': 'Male', 'Age': '12', 'Birthdate': '2010-11-07', 'Address': '부산 중구 59로 2'}, {'Id': '0a234508-1a52-4339-9e49-9c3dcf3d8d33', 'Name': '장은지', 'Gender': 'Female', 'Age': '37', 'Birthdate': '1985-12-25', 'Address': '광주 서구 31길 41'}, {'Id': '3166575b-82ca-4327-8992-767848e2afa9', 'Name': '최은지', 'Gender': 'Female', 'Age': '51', 'Birthdate': '1971-10-08', 'Address': '서울 남구 21길 78'}, {'Id': 'e09c5eea-b984-473f-98be-7fa81361e86e', 'Name': '이서준', 'Gender': 'Female', 'Age': '35', 'Birthdate': '1987-08-10', 'Address': '서울 중구 52길 26'}, {'Id': '38957748-049e-44b6-8c3e-5acfadfdedf2', 'Name': '조예진', 'Gender': 'Female', 'Age': '15', 'Birthdate': '2007-12-15', 'Address': '서울 남구 34로 97'}, {'Id': '5d11492a-3d41-4241-ab3b-312c68372937', 'Name': '이예지', 'Gender': 'Female', 'Age': '29', 'Birthdate': '1993-08-14', 'Address': '서울 서구 49 로 7'}, {'Id': 'c1da6b3f-51ad-4fc4-8143-5d2b161f44ee', 'Name': '최서준', 'Gender': 'Female', 'Age': '42', 'Birthdate': '1981-01-25', 'Address': '대구 강남구 25길 95'}, {'Id': 'b94a544a-87a0-4696-9863-eb3b1c140291', 'Name': '윤예진', 'Gender': 'Female', 'Age': '25', 'Birthdate': '1998-05-08', 'Address': '서울 중구 57로 91'}, {'Id': '6e637126-f456-449a-b310-361026e68f6a', 'Name': '조예준', 'Gender': 'Female', 'Age': '26', 'Birthdate': '1996-10-13', 'Address': '부산 남 구 82로 61'}, {'Id': 'eaff5dba-872a-4a6d-a3de-b16e1011b511', 'Name': '강지현', 'Gender': 'Male', 'Age': '39', 'Birthdate': '1983-08-17', 'Address': '광주 중 구 5길 90'}, {'Id': 'e6781d79-f7dc-4dbf-9d7c-f744738ac67c', 'Name': '박수호', 'Gender': 'Male', 'Age': '30', 'Birthdate': '1993-04-04', 'Address': '인천 서구 35로 8'}, {'Id': 'ead0a001-fa59-4f08-a40d-ff375e017653', 'Name': '김지훈', 'Gender': 'Female', 'Age': '49', 'Birthdate': '1973-11-24', 'Address': '서울 강서구 19로 10'}, {'Id': '16dccef2-f5df-47ae-b54a-cd1c626e91a1', 'Name': '윤지아', 'Gender': 'Female', 'Age': '41', 'Birthdate': '1981-07-03', 'Address': '부산  강남구 90로 64'}, {'Id': '2a912b2d-d8fc-44d1-856a-651cee31f9a6', 'Name': '조지아', 'Gender': 'Female', 'Age': '26', 'Birthdate': '1997-01-26', 'Address': '광주 중구 46길 6'}, {'Id': '93b71d05-4dd6-4a0c-bbb1-75aad38480fd', 'Name': '임민수', 'Gender': 'Male', 'Age': '30', 'Birthdate': '1993-04-05', 'Address': '인천 중구 15길 94'}, {'Id': '9d51a46c-780e-439e-97fc-86465b95ebab', 'Name': '박아윤', 'Gender': 'Female', 'Age': '37', 'Birthdate': '1986-05-28', 'Address': '부 산 강서구 46로 5'}, {'Id': '096f8679-7bbc-442f-b135-c530f98d0a8f', 'Name': '최성민', 'Gender': 'Female', 'Age': '13', 'Birthdate': '2009-06-22', 'Address': '광주 중구 38길 45'}, {'Id': 'aa927e62-7fb6-4807-831e-c7de4e604cfd', 'Name': '김하린', 'Gender': 'Male', 'Age': '30', 'Birthdate': '1993-02-06', 'Address': ' 서울 강서구 32길 37'}, {'Id': '44fcdee2-e600-4bd1-b86a-43ae3ca41d14', 'Name': '김하윤', 'Gender': 'Female', 'Age': '52', 'Birthdate': '1971-05-26', 'Address': '부산 남구 83로 41'}, {'Id': 'cb5cbf9f-3945-45bc-9579-b582d4a269b1', 'Name': '장아린', 'Gender': 'Female', 'Age': '23', 'Birthdate': '1999-11-23', 'Address': '인천 강남구 56로 4'}, {'Id': '0ce3e60c-ce9b-4c32-a8a1-61aaef3d2fcb', 'Name': '윤아윤', 'Gender': 'Male', 'Age': '47', 'Birthdate': '1976-03-04', 'Address': '부산 남구 4길 31'}, {'Id': '102ca5f7-909a-4bdf-8fa5-a4575b6bf172', 'Name': '강수빈', 'Gender': 'Male', 'Age': '19', 'Birthdate': '2004-04-11', 'Address': '대구 남구 78길 59'}, {'Id': '0f21dea4-02e7-43dc-9ec2-03b621702558', 'Name': '김준영', 'Gender': 'Female', 'Age': '32', 'Birthdate': '1991-03-11', 'Address': '광주 중구 34로 27'}, {'Id': '4b7d5483-6463-4046-a817-747604b17f19', 'Name': '이현지', 'Gender': 'Male', 'Age': '42', 'Birthdate': '1980-09-27', 'Address': '광주 강남구 47로 98'}, {'Id': '33a4f3f7-fd48-46b4-bf9e-c2f0be09cd3a', 'Name': '정지아', 'Gender': 'Male', 'Age': '26', 'Birthdate': '1997-01-21', 'Address': '부산 강서구 38로 100'}, {'Id': '9dc3e937-587a-42fa-b17d-b11642fe0f7d', 'Name': '강이안', 'Gender': 'Female', 'Age': '19', 'Birthdate': '2004-04-22', 'Address': '부산 서구 42로 6'}, {'Id': '1ae0c37e-5bc6-4b0b-876b-fab749e171f9', 'Name': '조이안', 'Gender': 'Male', 'Age': '46', 'Birthdate': '1976-06-15', 'Address': '서울 강남구 39길 97'}, {'Id': '1ffc16e0-f13a-4123-96d5-849c435deecc', 'Name': '조예진', 'Gender': 'Female', 'Age': '45', 'Birthdate': '1977-12-13', 'Address': '광주 남구 74로 24'}, {'Id': '7ec2af3b-b86b-4abe-8b58-356ca74c0aa1', 'Name': '정준혁', 'Gender': 'Male', 'Age': '28', 'Birthdate': '1994-10-02', 'Address': '인천 남구 48길 46'}, {'Id': '0a678f31-09b1-421a-9811-2a03a3d09218', 'Name': '장승현', 'Gender': 'Female', 'Age': '40', 'Birthdate': '1983-05-06', 'Address': '대구 강서구 9길 6'}, {'Id': '51127fb0-73ad-4945-a896-8c0f3b1f34c7', 'Name': '박승현', 'Gender': 'Female', 'Age': '28', 'Birthdate': '1994-11-27', 'Address': '광주 강남구 72로 91'}, {'Id': '788f833c-ee36-4e94-a7aa-c4d129894ae9', 'Name': '윤아린', 'Gender': 'Male', 'Age': '38', 'Birthdate': '1985-05-16', 'Address': '대구 강남구 86길 24'}, {'Id': '8efcfbb0-7c77-470e-9341-23011c62cc67', 'Name': '김도윤', 'Gender': 'Male', 'Age': '13', 'Birthdate': '2009-12-11', 'Address': '인천 강서구 84로 33'}, {'Id': '5152a69e-0dca-4366-b99b-6e7895befadf', 'Name': '임이안', 'Gender': 'Male', 'Age': '34', 'Birthdate': '1989-02-01', 'Address': '대구 서구 80로 80'}, {'Id': '6cf259ed-f64c-485e-b296-00c48ee92c65', 'Name': '장이안', 'Gender': 'Female', 'Age': '37', 'Birthdate': '1986-05-19', 'Address': '대구 서구 90로 38'}, {'Id': 'de4f5666-94b6-4aab-aad0-94b7329b1fbc', 'Name': '장이안', 'Gender': 'Male', 'Age': '25', 'Birthdate': '1998-03-02', 'Address': '광주 남구 75로 5'}, {'Id': 'e2c768fd-ff72-4c4f-b5f1-6bd352a67d71', 'Name': '최예지', 'Gender': 'Male', 'Age': '31', 'Birthdate': '1991-10-06', 'Address': '인천 남구 98로 78'}, {'Id': 'eb7349dc-5eb1-4d4b-bbc0-8f554229b366', 'Name': '최지원', 'Gender': 'Male', 'Age': '17', 'Birthdate': '2005-10-24', 'Address': '대구 중구 86길 20'}, {'Id': '31691f48-c19c-48eb-99eb-feabdf5a4cde', 'Name': '장지안', 'Gender': 'Male', 'Age': '40', 'Birthdate': '1983-03-11', 'Address': '인천 중구 63길 20'}, {'Id': 'a5a282c9-137f-42b1-8b2d-6433f663b1c0', 'Name': '강민석', 'Gender': 'Female', 'Age': '16', 'Birthdate': '2006-10-11', 'Address': '광주 강남구 92길 39'}, {'Id': '18a85fc1-6133-44c4-954b-e1ac8fedd97c', 'Name': '김준영', 'Gender': 'Female', 'Age': '34', 'Birthdate': '1989-04-11', 'Address': '부산 강서구 65로 3'}, {'Id': 'a41fc889-cd99-40ea-b2a6-1525c3f9f6f3', 'Name': '최준영', 'Gender': 'Female', 'Age': '12', 'Birthdate': '2010-06-11', 'Address': '서울 강남구 83로 93'}, {'Id': '06dcbb0c-68db-420d-9218-9519ef908e44', 'Name': '박성민', 'Gender': 'Male', 'Age': '16', 'Birthdate': '2006-06-15', 'Address': '서울 강서구 43길 77'}, {'Id': 'c72cc902-0d35-4bff-a944-1fb3bded2099', 'Name': '윤서윤', 'Gender': 'Female', 'Age': '24', 'Birthdate': '1998-12-10', 'Address': '인천 서구 44길 67'}, {'Id': 'f87ff0f4-b809-49cb-b0fe-68ad6435ce78', 'Name': '최하린', 'Gender': 'Female', 'Age': '34', 'Birthdate': '1988-11-25', 'Address': '인천 중구 53길 86'}, {'Id': '556ab94a-e782-49f0-a23c-55251ff06b88', 'Name': '임예지', 'Gender': 'Male', 'Age': '31', 'Birthdate': '1992-05-24', 'Address': '대구 강서구 81길 64'}, {'Id': '934bfac0-ed07-48ce-89ff-bfec277e77eb', 'Name': '강지안', 'Gender': 'Female', 'Age': '40', 'Birthdate': '1983-04-08', 'Address': '대구 강서구 21길 26'}, {'Id': '3b4514bb-48b4-41ca-b6ad-0cf514910c3d', 'Name': '윤현우', 'Gender': 'Female', 'Age': '30', 'Birthdate': '1992-09-17', 'Address': '광주 중구 21로 96'}]
result = [] 

# select문
# select * 
# from users
# where name = name and gender = gender

# for data in datas : 
#         if "강" in data['Name'] and "Male" == data['Gender'] :
#                 result.append(data)
# print(result)

max_size = 3
cur_page_num = 5

x = (cur_page_num/max_size)

start_index = max_size * (cur_page_num+(1/max_size))
end_index = max_size * (cur_page_num+1)

print(f"start-index : {start_index}\nend_index : {end_index}")