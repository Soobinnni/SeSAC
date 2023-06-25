import random
import datetime

class BirthdateGenerator:
    def generate_birthdate(self):
        while True:
            year = random.randint(1950, 2023)
            month = random.randint(1, 12)
            day = random.randint(1, 31)

            try:
                date = datetime.datetime(year, month, day)
                birth = date.strftime('%Y-%m-%d')  # 날짜 포맷
                return birth
            except ValueError:
                continue