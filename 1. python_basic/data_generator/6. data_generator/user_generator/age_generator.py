import random
import datetime

class AgeGenerator:
    def __init__(self):
        self.current_year = datetime.datetime.now().year
        self.birthdate_year = 0

    def get_age(self):
        return self.current_year - self.birthdate_year + 1