import random

class StoreTypeGenerator:
    def __init__(self):
        self.store_type_list = None
    
    def generate_store_type(self):
        return random.choice(self.store_type_list)
