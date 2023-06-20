users = [
    {"name" : "Alice", "age" : 25, "location" : "Seoul", "car" : "BMW"},
    {"name" : "Bob", "age" : 30, "location" : "Busan", "car" : "Mercedes"},
    {"name" : "Charlie", "age" : 35, "location" : "Daegu", "car" : "Audi"}
]
# 이름을 입력받아 사용자 정보(딕셔너리)를 반납하세요.
def find_users(name):
    result = []
    for c in users:
        if c['name'] == name:   
            result.append(c)
    return result

name = input()
print(find_users(name))


# 이름, 나이를 입력받아 사용자 정보(딕셔너리)를 반납하세요.
def find_name_age(name, age):
    result_name_age = []
    for a in users:
        if a['name'] == name and a['age']:
            result_name_age.append(a)
    return a

name_ = input()
age = input()
print(find_name_age(name, age))

# 이름, 나이, 사는 곳, 차를 입력
# find_users에서 계속 새로운 필드를 원할 때마다 함수의 인자가 늘어난다.
# 그래서 발생한느 문제가, 기존에 사용 중이던 모든 코드를 바꿔야 한다.
# find_users(name, age) => find_user(name, age, location)... 계속 바꿔야
# 문제 1. 어떻게 입력 인자를 효율적으로 받아서 처리하게 할까?

# 순회하여 비교하게 한다.
def find_users(name):
    result = []
    for c in users:
        if c['name'] == name:   
            result.append(c)
    return result
search_user = {
    "name" : "Bob",
    "age" : 30
}

#\줄바꿈에 대한 표시
def find_users(search_user):
    result = []
    for user in users:
        if user["name"] == search_user['name'] and \
            user["age"] == search_user['age']:
            result.append(user)
    return result



# 사용자로부터 문자(문장)을 입력 받아 대문자로 변환. upper() <-> lower()
def convert_case(text):
    example = ""
    for c in text:
        example += c.upper()
    # return dic_text
    return example

str = input()
print(convert_case(str))

# 사용자로부터 문자(문장)을 입력 받아 대문자면 소문자로, 소문자면 대문자로 변환. upper() <-> lower()
def convert_case(text):
        result = ""
        for c in text:
            if c.islower():
                 result += c.upper()
            elif c.isupper():
                 result += c.lower()
            else:
                result += c
        return result
text = input("문자열을 입력해주세요")
result = convert_case(text)                 

