# 1번
# - find_users(search_user) 함수를 완성하시오
# - search_user = {} 안에 있는 조건이 모두 매칭하는 사용자를 찾아내시오.
# - 예) {”name” : “Bob” } 이 있으면 이름으로만 검색
# - {”name” : “Bob”, “age” : 30}이 있으면 AND로 비교해서 검색하고 등
# - 문제 풀이 풀기.
users = [
    {"name" : "Alice", "age" : 25, "location" : "Seoul", "car" : "BMW"},
    {"name" : "Bob", "age" : 30, "location" : "Busan", "car" : "Mercedes"},
    {"name" : "Charlie", "age" : 35, "location" : "Daegu", "car" : "Audi"}
]
num_info = {
    1 : "name",
    2 : "age",
    3 : "location",
    4 : "car"
}

def get_user_input_list(search_num_list):
    # 사용자 입력 정보 리스트
    user_input_info_list = {}
    for num in search_num_list:
        #입력, 저장
        string_info = num_info[int(num)]
        comparison_info = input(string_info+'를 입력하세요.')
        #저장값을 딕셔너리에 저장
        user_input_info_list[string_info] = comparison_info

    return user_input_info_list
def find_users(user_input_list):
    for user_dict in users:
        #all() : 주어진 반복 가능한(iterable) 객체의 모든 요소가 참(True)인지를 판별하는 함수
        if all(user_dict[key] == user_input_list[key] for key in user_input_list):
            # 딕셔너리가 일치하는 경우
            print("일치하는 사용자:", user_dict)
        else:
            print('일치하는 사용자 없음')

# 입력
search_num_list = input('검색 정보를 선택하세요\n1.name 2.age 3.location 4.car\n(다중 선택 가능. 번호는 띄어쓰기로 구분하여 입력)').split()
user_input_list = get_user_input_list(search_num_list)
find_users(user_input_list)