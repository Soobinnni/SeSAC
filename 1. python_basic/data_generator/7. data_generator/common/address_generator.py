import random
class AddressGenerator:
    def __init__(self):
        self.usa_cities = []
        self.korea_cities = []
        self.korea_gus = []
        self.ADDRESS_MIN = 1 #상수
        self.ADDRESS_MAX = 99 #상수
  
    def generate_korea_address_list(self, num):
        city_name_list = random.choices(self.korea_cities, k=num)
        gu_name_list = random.choices(self.korea_gus, k=num)

        address_list = []

        for i in range(1, num):
            gil_num = str(random.randint(self.ADDRESS_MIN, self.ADDRESS_MAX))+'길'
            address_num = random.randint(self.ADDRESS_MIN, self.ADDRESS_MAX)
            address = city_name_list[i]+' '+gu_name_list[i]+' '+gil_num+ ' '+ str(address_num)

            address_list.append(address)
        
        return address_list
        
    def generate_usa_address(self):
        address_num = random.randint(1,50)
        city_name = random.choice(self.usa_cities)
        adresss = str(address_num) + ' ' +city_name
        return adresss
    