import random
import datetime

names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']

def generate_name():
    return random.choice(names)

def generate_gender():
    return random.choice(["female","male"])

def generate_birthdate():
    date = None
    year = random.randint(1950, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    try:
        date = datetime.datetime(year, month, day)
    except ValueError:
         generate_birthdate(birth)
    birth = date.strftime('%Y-%m-%d') #날짜 포맷
    return birth

def get_age(birth_year):
    current_year = datetime.datetime.now().year
    age = 0
    age = int(current_year) - int(birth_year) +1 #한국식 나이
    return age

def generate_address():
    return random.choice(cities)

def generate_individual_info():
    name = generate_name()
    gender = generate_gender()
    birth = generate_birthdate()
    age = get_age(birth[0:4])
    address = generate_address()

    individual_info = (name, gender, birth, age, address)

    return individual_info


# -----------------main
def main():
    # 이름, 성별, 생년월일, 나이 
    data_list = []

    print('name, gender, birth, age, address')
    for _ in range(1, 11): # range(a) == range(0,a)
        data_list.append(generate_individual_info())

    # 각각 출력
    for d in data_list:
        print(d)


# main 실행
main()    