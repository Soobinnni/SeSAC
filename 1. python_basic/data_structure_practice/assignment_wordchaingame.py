# 2번
# 응용개발 도서 4.5.2 및 5.3.5 의 끝말잇기를 레벨 1/2/3 단계로 나누어 각자 완성하시오.

# 컴퓨터의 낱말 리스트
computer_word_list = ["구멍", "게맛살", "글라이더", "기차", "대롱",
                       "더치페이", "롱다리", "리본", "멍게", 
                       "박쥐", "본네트", "빨대", "살구", 
                       "양심", "이빨", "이자", "자율", "주기", "쥐구멍", 
                       "차박", "트라이앵글"]

# 첫 문자 반환 함수
def cut_first_letter(string):
    return string[:1]
# 마지막 문자 반환 함수
def cut_last_letter(string):
    return string[-1:]
# 컴퓨터 대답 찾기
def get_response_word(user_word):
    result = ""
    for computer_word in computer_word_list:
        if (cut_last_letter(user_word) == cut_first_letter(computer_word)) and (computer_word not in response_list):
            result = computer_word
            return result
        else :
            continue
    return result
        
# 게임의 지속 여부
is_game_over = False

# 컴퓨터 / 사용자 응답, 응답 리스트
computer_response = '기차'
response_list = [computer_response]
user_response = ''

# 끝말잇기 시작
# 1단계
print("""<시작> 끝말잇기를 하자.
          만일, 생각나는 단어가 없다면 '졌어'를 입력해.
          내가 먼저 말할게. """)
while not is_game_over :
    print('<',computer_response,'>\n')
    user_response = input('제시 단어 입력 : ')
    if len(user_response) == 0:
        print('글자를 입력하지 않았어. 다시 입력해줘!')
        continue
    if len(user_response) == 1:
        print('한 글자는 반칙이야! <끝>')
        break
    if user_response == "졌어":
        print('내가 이겼어! <끝>')
        break
    elif cut_first_letter(user_response) != cut_last_letter(computer_response):
        print('글자가 안 이어져. 내가 이겼다!<끝>')
        break
    elif user_response in response_list:
        print('아까 했던 말이야. 내가 이겼어!<끝>')
        break
    else:
        response_list.append(user_response)
        # 문자열에 not 연산자를 사용하는 경우, 문자열이 비어있는지 여부를 판별할 수 있습니다. 
        # 비어있지 않은 문자열은 True로 평가되고, 비어있는 문자열은 False로 평가됩니다.
        computer_response = get_response_word(user_response)
        if not computer_response:
            print('모르겠다. 내가 졌어.<끝>')
            break
        else: 
            computer_word_list.remove(computer_response)
            response_list.append(user_response)
            continue


# 2단계
# 두음법칙을 적용

# 3단계