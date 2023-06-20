
#java와 마찬가지로 반환하는 값은 return과 함께
#하지만 반환 값이 두 개일 수 있다.
def get_name_and_age():
    return "John", 25

name, age = get_name_and_age()
print(name)
print(age)


#리스트(배열) : 형태 []
shopping_list = ["apple", "banana", "orange"]
print(shopping_list)

#리스트에 요소 추가 : append
shopping_list.append("grape")

#리스트에 요소 삭제 : remove
shopping_list.remove("banana")

#list 순회하기
numbers = [1, 2, 3, 4, 5]
for num in numbers:     
    print(num)

# 짝수만 출력하기
for num in numbers:  
    if num % 2 == 0:
        print(num, "is 짝수") 
    else:
        print(num, "is 홀수") 

# 홀수 리스트와 짝수 리스트를 따로 만들어서, 목록에 추가하시오
# even_numbers와 odd_numbers        
even_numbers = []
odd_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(even_numbers)  
print(odd_numbers)         

# 이 목록에서 90점 이상인 학생을 출력
student_grades = {
    "John" : 85,
    "Emily" : 92,
    "Michael" : 78,
    "Sophia" : 95
}
for student, grade in student_grades.items():
    print(student, grade)
for student, grade in student_grades.items():
    if grade>=90:
        print(student, grade)

               

#딕셔너리(Dictionary) cf. java - Map
#Key와 Value 자료구조 
# {}활용
student = {
    "name" : "kim",
    "age" : 26,
    "university" : "ABC uni"
}
print("Name : ", student['name'])
print("Age : ", student['age']) 

print("삭제 후 리스트 : ",shopping_list)

# 입력 cf. java : Scanner = python : input 