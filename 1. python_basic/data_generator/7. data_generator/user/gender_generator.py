import random

class GenderGenerator:
    #생성자
    def __init__(self):
      self.genders = ['female', 'male']

    def generate_gender(self):
        return random.choice(self.genders)
    
