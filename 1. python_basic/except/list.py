numbers = [1,2,3,4,5]

# value = numbers[5] # ! index 5가 없기 때문에 오류 발생

def get_number(index):
    if(index < len(numbers)):
        return numbers[index]
    else:
        return '오류'
print(get_number(5))
 
# 예외 처리
def get_number_2(index):
    try:    
        return numbers[index]
    except IndexError:
        return 'error : 입력 값에 대한 인덱스 번호가 잘못되었습니다.'
    except TypeError:
        return 'error : 입력 값의 유형이 잘못되었습니다.'

print(get_number_2('a'))
print(get_number_2(5))

# ----------------미션 1----------------
def convert_to_integer(num_str):
    #글자를 입력받아 숫자로 변환해서 반환
    try:
        convert_num = int(num_str)
        return convert_num
    except ValueError:
        return "error : 숫자로 전환 가능한 문자열이 아님"    
    
print(convert_to_integer("11"))
print(convert_to_integer("-5"))
print(convert_to_integer("5"))
print(convert_to_integer("7"))
print(convert_to_integer("A"))
print(convert_to_integer("HELLO"))
# ----------------미션 1-2 : 입력받은 글자를 숫자로 변환해서 +1을 반환----------------
def convert_to_integer_2(num_str):
    #글자를 입력받아 숫자로 변환해서 반환
    try:
        convert_num = int(num_str)
        return convert_num+1
    except ValueError:
        return "error : 숫자로 전환 가능한 문자열이 아님"
    
print(convert_to_integer_2("11"))
print(convert_to_integer_2("-5"))
print(convert_to_integer_2("5"))
print(convert_to_integer_2("7"))
print(convert_to_integer_2("A"))
print(convert_to_integer_2("HELLO"))

# ----------------미션 2 : 사용자로부터 입력 받아----------------
def convert_to_integer_3(num_str):
    #글자를 입력받아 숫자로 변환해서 반환
    # try:
    #     convert_num = int(num_str)
    #     return convert_num
    # except ValueError:
    #     return "error : 숫자로 전환 가능한 문자열이 아님"
    # return이 중간에 있으면 바람직한 코드가 아니기 때문에 끝으로 빼는 것을...
    value = None
    try:
        value = int(num_str)
    except ValueError:
        print("error : 숫자로 전환 가능한 문자열이 아님")
    return value
    
input_str_num = input('숫자로 전환 가능한 문자열(예: 2)을 입력하세요')   

print(convert_to_integer_3(input_str_num))


