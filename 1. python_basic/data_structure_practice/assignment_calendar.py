# 3번
# 3. 달력 만들기 (윤년/윤달 등 계산)
# calendar 라이브러리를 사용하지 않고, 직접 파이썬 함수를 통해 구현하시오.

# 0: 월요일
# 1: 화요일
# 2: 수요일
# 3: 목요일
# 4: 금요일
# 5: 토요일
# 6: 일요일

# ----------

# 연도를 입력하세요: 2023
# 월을 입력하세요: 6

# 6월 2023
# 일 월 화 수 목 금 토
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30

# 일수 계산
def get_days(year, month):
    days = 0
    thirty_months = [4,6,9,11]
    if month in thirty_months:
        days = 31
    elif month != 2:
        days = 30
    elif is_leap_year(year):
        days = 29
    else:
        days = 28


# 윤년 계산
    # 4로 나누어 떨어지는 해 == 윤년
    # 100으로 나누어 떨어지는 해 == 평년
    # 하지만 400으로 나누어 떨어지는 해 == 윤년
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# 해당 월의 첫 날의 요일을 계산
def get_first_day(y)
first_day = year * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400

# 달력은 빈 셀까지 28 또는 35 또는 42개의 셀을 갖는다.
first_day + 


# 빈 배열을 만든다.
days = []
for (var i = 0; i < cell; i++) {
    days[i] = {
        date: '',
        dayNum: '',
        today: false
    };
}

print(month,'월 ',year) 
for(i in range(1:n)):
