import random

class StoreTypeGenerator:
    def __init__(self):
        self.store_type_list = None
    
    def generate_store_type(self, num):
        return random.choices(self.store_type_list, k=num)
