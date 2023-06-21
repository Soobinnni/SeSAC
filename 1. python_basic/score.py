# 사용자로부터 점수를 입력받는다.
# 사용자로부터 이름을 입력받ㄷ는다
# 이 점수가 최고 점수면 하이스코어를 기록한다.
# 'high'라고 입력하면 현재까지의 하이스코어와 그 사람이 누군지 출력한다
# 'history'라고 입력하면 그 동안 입력한 모든 점수와 사람을 출력한다.


# -----------------전역변수----------------
high_score = (None, None) #튜플(사용자, 점수)
history_array = [high_score] #

w_exit = True
# -----------------각종함수----------------
def choice_menu():   
    choice = None
    menu_list = ["input", "history", "high"]

    # 메뉴 소개
    print('1. 점수 입력) : input을 입력하세요')
    print('2. 최고 점수 확인) : high를 입력하세요')
    print('3. 점수 이력 확인) history를 입력하세요')
   
    # 사용자 메뉴 입력
    choice = input()   

    if choice not in menu_list:
        print('보기 안 ')


    #리턴
    return choice
    
       

    


if menu_choice not in menu_list:
    print('메뉴 입력을 다시 해주세요')

if menu_choice == 'input':
    input_score = int(input())
    # history에 올리고, 가장 높은 점수일 경우 high의 value를 대체한다.
    scores["history"].append(input_score) # history에 올림
    if scores["high"] == None:
        scores["high"] = input_score
    elif scores["high"] <= input_score:
        scores["high"] = input_score
        

elif menu_choice == 'high':
    print(f'{scores["high"]}')
elif menu_choice == 'history':
    print(f'{scores["history"]}')


# -----------------메인함수----------------
def main():
    while True:
        op = choice_menu()
        if op == 'score':
            score, name = input_score()
            score_result(score, name)
        elif op == 'history':
            print_history
        elif op == 'high':
            print_highscore


#------------------------------------------------------------------------------------------------------수업에서 짠 내용

# -----------------전역변수----------------
game_history = []
high_score = None
# -----------------각종함수----------------
def input_score():
    score = int(input("점수 : "))
    name = input("이름 : ")

    return score, name

def score_result(score, name):
    game_score = (score, name) #튜플
    game_history.append(game_score)

    if(score > high_score):
        high_score = score

def print_history():
    print('--------------------')
    print('점수, 이름')
    print('--------------------')
    print(game_history)
    

def print_highscore(highscore):
    print('--------------------')
    print(f'최고 점수 : {high_score}')
    high = 0

    for score, _ in game_history: #    for score, name in game_history: 이지만, name은 받아오곤 싶지만 사용하지 않는 변수일 떄 '_'로 표시만
        if score > high_score:
            high_score = score

    #점수가 많아지면? 매번 high score를 가져오기 위해서 해야 하는 연산 량이 너무 많음
    # 알고리즘에 대한 고민
def input_mode():
    mode_ops = ['score', 'high', 'history']
    mode = input(' 입력모드 입력 : ')
    if mode not in mode_ops:
        mode = input("입력 모드 없음. 재입력")

    return mode
# -----------------메인함수----------------
# if __name__ == "__main__":

def main():
    while True:
        op = input_mode()
        if op == 'score':
            score, name = input_score()
            score_result(score, name)
        elif op == 'history':
            print_history
        elif op == 'high':
            print_highscore

# -----------------메인함수 실행----------------
main()

