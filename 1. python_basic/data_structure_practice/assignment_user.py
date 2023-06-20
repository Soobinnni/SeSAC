# # 1번
# # - find_users(search_user) 함수를 완성하시오
# # - search_user = {} 안에 있는 조건이 모두 매칭하는 사용자를 찾아내시오.
# # - 예) {”name” : “Bob” } 이 있으면 이름으로만 검색
# # - {”name” : “Bob”, “age” : 30}이 있으면 AND로 비교해서 검색하고 등
# # - 문제 풀이 풀기.
users = [
    {"name" : "Alice", "age" : 25, "location" : "Seoul", "car" : "BMW"},
    {"name" : "Bob", "age" : 30, "location" : "Busan", "car" : "Mercedes"},
    {"name" : "Charlie", "age" : 35, "location" : "Daegu", "car" : "Audi"}
]
# num_info = {
#     1 : "name",
#     2 : "age",
#     3 : "location",
#     4 : "car"
# }

# def get_user_input_list(search_num_list):
#     # 사용자 입력 정보 리스트
#     user_input_info_list = {}
#     for num in search_num_list:
#         #입력, 저장
#         string_info = num_info[int(num)]
#         comparison_info = input(string_info+'를 입력하세요.')
#         #저장값을 딕셔너리에 저장
#         user_input_info_list[string_info] = comparison_info

#     return user_input_info_list
# def find_users(user_input_list):
#     for user_dict in users:
#         #all() : 주어진 반복 가능한(iterable) 객체의 모든 요소가 참(True)인지를 판별하는 함수
#         if all(user_dict[key] == user_input_list[key] for key in user_input_list):
#             # 딕셔너리가 일치하는 경우
#             print("일치하는 사용자:", user_dict)
#         else:
#             print('일치하는 사용자 없음')

# # 입력
# search_num_list = input('검색 정보를 선택하세요\n1.name 2.age 3.location 4.car\n(다중 선택 가능. 번호는 띄어쓰기로 구분하여 입력)').split()
# user_input_list = get_user_input_list(search_num_list)
# find_users(user_input_list)


# def find_users_2(seacrch_user):
#     result = []
#     for user in users:
#         if(seacrch_user.get("name") is None or seacrch_user.get("name")== user.get("name")) and\
#         (seacrch_user.get("age") is None or seacrch_user.get("age")== user.get("age")) and\
#         (seacrch_user.get("location") is None or seacrch_user.get("location")== user.get("location")) and\
#         (seacrch_user.get("car") is None or seacrch_user.get("car")== user.get("car")):
#             result.append(user)

#     return result

# result = find_users_2('Alice')

# def matches_criteria(user, condition):
#     for key, value in condition.items():
#         if user.get(key) != value:
#                 return False
#     return True

# def find_users_3(search_user):
#     result = []
#     for user in search_user:
#         if matches_criteria(user, search_user):
#             result.append(user)

#     return result

# 우리가 구현한 하나의 함수를 구동하며 이 다섯 개의 테스트 케이스를 실행한다.
# 그래서 기대한 결과가 나오는지 보고
# 모두 다 성공하면 화면에 'PASS'를 출력하고 하나라도 실패하면 화면에 FAIL을 출력한다.
users = [
    {"name" : "Alice", "age" : 25, "location" : "Seoul", "car" : "BMW"},
    {"name" : "Bob", "age" : 30, "location" : "Busan", "car" : "Mercedes"},
    {"name" : "Charlie", "age" : 35, "location" : "Daegu", "car" : "Audi"}
]
def matches_criteria(user, condition):
    for key, value in condition.items():
        if user.get(key) != value:
                return False
    return True

def find_users_3(search_user):
    result = []
    for user in users:
        if matches_criteria(user, search_user):
            result.append(user)
    if len(result) != 0:
        return len(result)
    else:
         return len(result)

search_bob1 = {"name" : "Bob"}
search_bob2 = {"age": 30}
search_bob3 = {"name" : "Bob", "age": 30}
search_bob4 = {"name" : "Bob", "age": 31}
search_bob5 = {}

print(find_users_3(search_bob1))
print(find_users_3(search_bob2))
print(find_users_3(search_bob3))
print(find_users_3(search_bob4))
print(find_users_3(search_bob5))

# def test_find_users():
#     final_result = False

#     if not (find_users(search_bob1))

# search_result_count = [1, 1, 1, 0, 3]
# search_info_list = [find_users_3(search_bob1), find_users_3(search_bob2),\
#                      find_users_3(search_bob3), find_users_3(search_bob4), find_users_3(search_bob5)]

# def test_find_users():
#     final_result = True

#     for i in range(0,5):
#      if search_result_count[i] == search_info_list[i]:
#          final_result = True
#     return final_result    

# print(test_find_users())

        
    #  final_result = True
    #  if not find_users_3(search_bob1) == 1:
    #       final_result =False
    #  if not find_users_3(search_bob2) == 1:
    #       final_result =False
    #  if not find_users_3(search_bob3) == 1:
    #       final_result =False
    #  if not find_users_3(search_bob4) == 0:
    #       final_result =False
    #  if not find_users_3(search_bob5) == 3:
    #       final_result =False
            
    #  return final_result



search_result_count = [1, 1, 1, 0, 3]
search_info_list = [search_bob1, search_bob2, search_bob3, search_bob4, search_bob5]


def test_find_users():
    final_result = True

    for i, search_info in enumerate(search_info_list):
        if find_users_3(search_info) == search_result_count[i]:
            final_result = True
    if final_result:
        return 'PASS'
    else:
        return 'FAIL'    

print(test_find_users())



# -------------------------- enumerate함수를 사용하여 배열의 값들을 비교.--------------------------
search_result_count = [1, 1, 1, 0, 3]
search_info_list = [search_bob1, search_bob2, search_bob3, search_bob4, search_bob5]


def test_find_users():
    final_result = True

    for i, search_info in enumerate(search_info_list):
        if find_users_3(search_info) == search_result_count[i]:
            final_result = True
    if final_result:
        return 'PASS'
    else:
        return 'FAIL'    

print(test_find_users())

# ------------------------딕셔너리에 값을 의미 있게 담아서 값을 순회하며 비교----------------------------
test_cases = [
    {"case" : search_bob1, "expected_result" : 1},
    {"case" : search_bob2, "expected_result" : 1},
    {"case" : search_bob3, "expected_result" : 1},
    {"case" : search_bob4, "expected_result" : 0},
    {"case" : search_bob5, "expected_result" : 3}
]

def test_find_users():
    final_result = True

    for test_case in test_cases:

        case = test_case['case']
        expected_result = test_case['expected_result']

        if find_users_3(case) == expected_result:
            final_result = True
    if final_result:
        return 'PASS'
    else:
        return 'FAIL'    

print(test_find_users())