import random

class StoreNameGenerator:
    def __init__(self):
        self.store_type = None
        self.store_place_list = None
    
    def generate_store_name(self, store_type):
        store_num = random.randint(1, 10)
        store_place = random.choice(self.store_place_list)
        store_name = store_type + ' ' + store_place + str(store_num) + '호점'

        return store_name