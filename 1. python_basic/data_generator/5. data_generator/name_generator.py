import random

class NameGenerator:
    def __init__(self):
            self.names = []
      
    def generate_name(self):
        return random.choice(self.names)