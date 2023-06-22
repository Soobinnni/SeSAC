import random

class NameGenerator:
    def __init__(self):
            self.usa_names = []
            self.korean_last_names = []
            self.korean_first_names = []
      
    def generate_korean_name(self): 
        korean_first_name = random.choice(self.korean_first_names)
        korean_last_name = random.choice(self.korean_last_names)
       
        korean_name = korean_last_name + korean_first_name
        return korean_name
      
    def generate_usa_name(self):
        return random.choice(self.usa_names)