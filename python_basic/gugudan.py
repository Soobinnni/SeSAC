# range함수를 이용한다.
for i in range(2, 9):
	for j in range(1, 10):
		print(i, '*', j, '=', i*j)
		
# 포맷팅 한다.        
for i in range(2, 9):
	print(f"{i}단")
	for j in range(1, 10):
		print(f"{i} X {j} = {i *j}")
		
# 함수화 하기         
def gugudan():
    print('함수를 이용한 구구단 프린트')
    for i in range(2, 9):
        print(f"{i}단")
        for j in range(1, 10):
            print(f"{i} X {j} = {i *j}")

gugudan()