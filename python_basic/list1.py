# 1부터 10까지의 각 숫자의 제곱으로 이루어진 목록을 만들 때.
squares = []
for x in range(1, 11):
    squares.append(x ** 2) #x의 제곱들을 범위만큼 리스트에 추가

print(squares)    

squares = [ x ** 2]
squares = [ x ** 2 for x in range(1,11)] # 뒤에 내가 정의한 변수의 생성 방식을 정의(for문을 앞서 3줄로 정의하던 것을 요약할 수 있음)

# 1부터 20까지의 짝수들로 리스트를 생성하시오
even_numbers = []
even_numbers = [x] # 내가 원하는 숫자를 표현할 정수
#even_numbers = [x ....]
even_numbers = [x for x in range(1,21)]
even_numbers = [x for x in range(1,21) if x % 2 == 0]
                
print(even_numbers)


# ---------------------------------------------------
# 문자열의 각 글자를 순회하면서 대문자로 바꾸시오
# 출력 : ['H', 'E', ... , 'O']
# .upper() : 대문자 전환
word = "hello"
word = word.upper()
# 문자열은 순회가능한 데이터이기 때문에 아래와 같이 표현하여 순회할 수 있다.
upper_letters = [c for c in word]
print(upper_letters)

# 문자열 길이가 3 이하인 단어들만 선택하기
words = ["apple", "banana", "cherry", "dragonfruit", "egg"]
short_words = []
short_words = words
for c in words:
    if len(c)<=3:
        print(c)
