# 계산기 만들기
# 사용자로부터 입력을 받아서 계산. 
# 연산모드를 입력받는다. - 덧셈, 뺄셈, 곱셈, 나눗셈
# 숫자를 두 개 입력 받는다.
# 그래서 결과를 보여준다.
# 실행 예시)
# 연산모드를 입력하시오 : plus minus multiply division
# 숫자 1을 입력하시오 : 
# 숫자 2을 입력하시오 : 
# 결과 : 


# 연산자 검사 및 반환
def input_operator():
    incorrect_input = True
    operator_list = ['plus', 'minus', 'multiply', 'division']
    while incorrect_input:
        input_operator =input()

        if input_operator in operator_list:
            incorrect_input = False
            return input_operator
        else:
            print('보기에 있는 연산자를 입력해주세요.\nplus\n minus\n multiply\n division')
            incorrect_input = True

def input_val():
    val = None
    incorrect_input = True
    while incorrect_input:
        val = input()
        try:
            val = int(val)
            incorrect_input = False
            return val
        except ValueError:
            incorrect_input = True
            print("숫자를 입력해주세요")

print('계산기 프로그램\n 연산기호를 입력하시오\nplus\n minus\n multiply\n division')
operator = input_operator()   
print('숫자 1을 입력하세요')      
val1 = input_val()
print('숫자 2을 입력하세요')      
val2 = input_val()
    
# 계산 수행
result = 0
if(operator=='plus'):
    result = val1+ val2
elif(operator=='minus'):
    result = val1- val2
elif(operator=='multiply'):
    result = val1 * val2
elif(operator=='division'): 
    try:
        result = val1 / val2
    except ZeroDivisionError:
        print('나누는 값이 0이 될 수 없습니다.')
        result = None

print(f'연산 결과 : {result}')
    



# ----------------------------------------
# mode = val1 = val2 = None

# operator_list = ['plus', 'minus', 'multiply', 'division']

# def input_mode():
#     mode = input('연산모드를 입력하시오')
#     if mode not in operator_list:
#         print('올바른 연산자가 입력되지 않았습니다.')
#         print('다시 입력해주세요')
#         input_mode()
#     else:
#         return mode

# def input_values1():
#     try:
#         val1 = int(input('숫자1을 입력하시오: '))
#         return val1
#     except ValueError : 
#         print('올바른 숫자가 입력되지 않았습니다.')
#         print('다시 입력해주세요')
#         val1 = input_values1() #함수 재호출

# def input_values2():
#     try:
#         val2 = int(input('숫자2를 입력하시오: '))
#         return val2
#     except ValueError : 
#         print('올바른 숫자가 입력되지 않았습니다.')
#         print('다시 입력해주세요')
#         val2 = input_values2() #함수 재호출


# mode = input_mode()
# print(mode)
# val1 = input_values1()
# print(val1)
# val2 = input_values2()
# print(val2)

# def operation(mode, val1, val2):
#     result = None
#     if(mode=='plus'):
#         result = val1+ val2
#     elif(mode=='minus'):
#         result = val1- val2
#     elif(mode=='multiply'):
#         result = val1 * val2
#     elif(mode=='division'): 
#         try:
#             result = val1 / val2
#         except ZeroDivisionError:
#             print('0으로 나눗셈을 할 수 없습니다.')
#             result = None
#     return result

# result = operation(mode, val1, val2)
# print(f'계산 결과 : {result}')

# # ZeroDivisionError : 나누는 값이 0일 때 오류







