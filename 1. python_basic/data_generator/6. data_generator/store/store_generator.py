from generator import Generator

from store.store_name_generator import StoreNameGenerator
from common.address_generator import AddressGenerator
from store.store_type_generator import StoreTypeGenerator

class StoreGenerator(Generator):
#  - M6. 위 내용들을 참조해서 새로운 타입인 상점(store) 데이터를 생성하시오. (독립적인 코드로 구성)
#    상점의 이름, 타입(커피샵 유형), 주소를 생성하시오
    def mk_store_type(self):
        store_type_instance = StoreTypeGenerator()
        store_type_instance.store_type_list = self.file_to_list("store_types.txt")
        store_type = store_type_instance.generate_store_type()

        return store_type
    
    def mk_store_name(self, store_type):
        store_name_instance = StoreNameGenerator()
        store_name_instance.store_place_list = self.file_to_list("store_places.txt")
        store_name = store_name_instance.generate_store_name(store_type)

        return store_name

    def mk_store_address(self):
        address_instance = AddressGenerator()
        address_instance.korea_cities = self.file_to_list("korea_cities.txt")    
        address_instance.korea_gus = self.file_to_list("korea_gus.txt")      
        address = address_instance.generate_korea_address()

        return address

    def generate_info(self):
        individual_store_dic = {
            "id" : None,
            "name" : None,
            "type" : None,
            "address" : None
        }       
        individual_store_dic['id'] = self.mk_uuid()
        individual_store_dic['type'] = store_type = self.mk_store_type()
        individual_store_dic['name'] = self.mk_store_name(store_type)
        individual_store_dic['address'] = self.mk_store_address()

        return individual_store_dic