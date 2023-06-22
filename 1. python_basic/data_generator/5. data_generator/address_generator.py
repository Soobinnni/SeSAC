import random
class AddressGenerator:
    def __init__(self):
        self.cities = []
    
    def generate_address(self):
        address_num = random.randint(1,50)
        city_name = random.choice(self.cities)
        adresss = str(address_num) + ' ' +city_name
        return adresss
    