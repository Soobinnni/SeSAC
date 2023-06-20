import math

# ----------------------원의 넓이를 구하기----------------------
def get_area(radius):
    return math.pow(radius, 2) * math.pi
    # return radius * radius * math.pi
    # return radius * radius * 3.14

radius = 5
area = get_area(radius)

# ----------------------무작위 숫자 생성----------------------
import random
# radnint에 대한 설명
# def randint(self, a, b): 
#         """Return random integer in range [a, b], including both end points."""
#         return self.randrange(a, b+1)
def roll_dice():
    dice_roll = random.randint( 1, 6 )
    print(dice_roll)

# 주사위를 10번 던져서 나온 수를 출력
for i in range(1, 11):
    roll_dice()

# 이 리스트를 무작위로 섞기
my_list = [1,2,3,4,5]

def shuffle():
    # 무작위 숫자를 생성해서
    # my_list에서 그 숫자의 인덱스의 번호를 골라서
    # 새 리스트에 추가한다.
    # 이걸 반복한다.
    my_new_list = []
    list_len = len(my_list)
    for i in range(0, list_len):
        pick = random.randint(0, list_len-i-1)
        my_new_list.append(my_list[pick])
        my_list.remove(my_list[pick])

    return my_new_list

print("원본 리스트 : ", my_list)
random.shuffle(my_list) # 복제본이 아니라 원본을 섞기 때문에 random.shuffle 후 원본이 뒤섞여 있다.
print("섞인 리스트 : ", my_list)

