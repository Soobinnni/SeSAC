# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음

name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크: 공격 유닛, 탱크 포를 쏠 수 있음. 일반모드/시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage): #이름, 공격방향, 공격데미지
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(name, location, damage))


attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)

# 끝없는 반복 생성...

# >> 클래스를 만들고 그의 인스턴스를 활용하여 그의 속성과
# >> 행위를 가져다 쓰는 것이 효율적

class Unit:
    def __init__(self, name, hp, damage):
        self.name =name 
        self.hp = hp
        self.damage = damage

        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

marine1 = Unit("마린", 50, 5)
tank = Unit("탱크", 150, 35)