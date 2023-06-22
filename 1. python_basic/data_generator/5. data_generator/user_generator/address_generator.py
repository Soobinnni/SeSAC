import random
class AddressGenerator:
    def __init__(self):
        self.usa_cities = []
        self.korea_cities = []
        self.korea_gus = []

    
    def generate_korea_address(self):
        city_name = random.choice(self.korea_cities)
        gu_name = random.choice(self.korea_gus)
        gil_num = str(random.randint(1,50))+'길'
        address_num = random.randint(1,50)
        adresss = city_name+' '+gu_name+' '+gil_num+ ' '+ str(address_num)
        
        return adresss
        
    def generate_usa_address(self):
        address_num = random.randint(1,50)
        city_name = random.choice(self.usa_cities)
        adresss = str(address_num) + ' ' +city_name
        return adresss
    