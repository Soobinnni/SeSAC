# ; ### 미션1

# ; - 이름, 성별, 나이, 생년월일, 주소를 생성한다.
# ; ```
# ; - M1. 10명의 사람의 이름을 랜덤으로 생성하시오. (영문 이름 샘플 10개 참조해서)
# ; - M1-2. 성별, 생년월일, 나이를 랜덤으로 생성하시오. (나이 주의 = 생년월일 기반 계산)
# ; - M1-3. 주소를 랜덤으로 생성하시오.
import random
import datetime

names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
birth = {
    "year" : range(1900,2023),
    "month" : range(1,13),
    "day" : range(1,32)
}
individual_info_dic = {
    "name" : None,
    "gender" : None,
    "birth" : None,
    "age" : None,
    "address" : None
}

def generate_name():
    return random.choice(names)

def generate_gender():
    return random.choice(["female","male"])

def generate_birthdate(birth):
    date = None
    year = int(random.choice(birth["year"]))
    month = int(random.choice(birth["month"]))
    day = int(random.choice(birth["day"]))

    try:
        date = datetime.datetime(year, month, day)
    except ValueError:
         generate_birthdate(birth)
    birth = date.strftime('%Y-%m-%d') #날짜 포맷
    return birth
# def generate_birthdate(birth):
#     year = random.choice(birth["year"])
#     month = random.choice(birth["month"])
#     if(month < 10):
#         month = '0'+str(month)
#     day = random.choice(birth["day"])
#     if(day < 10):
#         day = '0'+str(day)

#     birth = str(year)+'-'+str(month)+'-'+str(day)
#     return birth

def get_age(birth_year):
    current_year = datetime.datetime.now().year
    age = 0
    age = int(current_year) - int(birth_year) +1 #한국식 나이
    return age

def generate_address():
    return random.choice(cities)

def generate_individual_info(birth):
    individual_info_dic['name'] = generate_name()
    individual_info_dic['gender'] = generate_gender()
    individual_info_dic['birth'] = generate_birthdate(birth)
    individual_info_dic['age'] = get_age(individual_info_dic['birth'][0:4])
    individual_info_dic['address'] = generate_address()

    return individual_info_dic


# -----------------main
def main():
    # 이름, 성별, 생년월일, 나이 
    data_list = []
    ex_list = []

    for i in range(1,11):
        ex_list.append(i)

    for _ in range(1, 11): # range(a) == range(0,a)
        individual_info_dic = generate_individual_info(birth)
        print(individual_info_dic)
        data_list.append(individual_info_dic)

    # 각각 출력
    # for d in data_list:
    #     print(d)
    print(data_list)
    print(ex_list)


# main 실행
main()    

# ; ```

# ; - 결과물 예시

# ; ```bash
# ; Name,Birthdate,Gender,Address
# ; Jane,1990-01-03,Male,50 New York
# ; Jane,1990-04-14,Male,46 Philadelphia
# ; Jane,1981-01-07,Male,69 Los Angeles
# ; Emily,1975-09-03,Female,33 Philadelphia
# ; Olivia,1987-12-18,Male,2 Chicago
# ; Michael,1980-03-21,Male,18 Chicago
# ; Michael,1982-03-02,Male,57 Houston
# ; Olivia,1976-10-19,Female,36 Chicago
# ; Emily,1976-01-05,Female,96 New York
# ; ...
# ; ```


