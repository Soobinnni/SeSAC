import random

class NameGenerator:
    def __init__(self, names):
            self.names = names
      
    def generate_name(self):
        return random.choice(self.names)