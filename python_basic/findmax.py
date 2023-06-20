numbers = [3, 7, 2, 9, 1, 4]

def find_max(num_list):
    #입력받은 인자의 리스트 중에서 가장 큰 숫자를 반납하시오
    a = numbers[0]
    # a = 0 : 모든 요소가 음수일 때, 리스트에서 최댓값을 찾지 않고 0으로 최댓값을 출력하기에 오류 발생
    for c in numbers:
        if a < c:
            a = c
    return a

print("최댓값: ", find_max(numbers))
#-----------------------------------------------------------------------------
numbers2 = [1, 2,3,4,5,4,3,2,6,7,3,2,1,6]
def remove_duplicate(num_list):
    new_num_list = []
    for num in numbers2:
        if not num in new_num_list:
            new_num_list.append(num)
        # if  num in new_num_list:
        #     continue 키워드 사용해서 계속 진행
        # else:
        #     new_num_list.append(num)   
    return new_num_list

print('원본리스트 : ', numbers2)
print('중복 제거리스트 : ', remove_duplicate(numbers2))
#-----------------------------------------------------------------------------
# 미션 2. 아래 내용을 한 줄로 작성하시요(파이썬 기능/함수를 최대한 사용해서)
unique_list = list(set(numbers2)) #set은 순서를 고려하지 않기 때문에 set을 list로 반환하여 순서 유지
print("함수를 사용한 중복 제거 : ",unique_list)


# 사용자로부터 입력 받아서, 공백(스페이스)으로 구분된 문자열을 입력받아서, 그 안에서 MAX를 구하시오.
# input()입력 받아서 그 리스트 내에서 MAX를 구하시오, string을 int로 변환하기(int()함수)
def find_max2(num):
    num_list = num.split()
    listaaaa = []
    for string in num_list:
        listaaaa.append(int(string))
    return max(listaaaa)
    # 함수 재사용 : return find_max(num)
user_input = input("숫자를 입력하시오(공백으로 구분된)")
max_number = find_max2(user_input)
print(max_number)


# 미션 3. 리스트 컴프리헨션을 사용해서 위의 복잡한 과정을 1줄로 변경하시오.
def find_max3(string):
    num_list = [int(num) for num in string.split()]
    return max(num_list)
    # 함수 재사용 : return find_max(num)
user_input = input("숫자를 입력하시오(공백으로 구분된)")
max_number2 = find_max3(user_input)
print(max_number2)