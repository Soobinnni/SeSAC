from common.generator import Generator
from common.address_generator import AddressGenerator
from common.file_reader import FileReader

from store.store_name_generator import StoreNameGenerator
from store.store_type_generator import StoreTypeGenerator

class StoreGenerator(Generator):
#  - M6. 위 내용들을 참조해서 새로운 타입인 상점(store) 데이터를 생성하시오. (독립적인 코드로 구성)
#    상점의 이름, 타입(커피샵 유형), 주소를 생성하시오
    # def mk_store_type_list(self, num):
    #     store_type_instance = StoreTypeGenerator()
    #     store_type_instance.store_type_list = FileReader().file_to_list("store_types.txt")
    #     store_type_list = store_type_instance.generate_store_type(num)

    #     return store_type
    
    def mk_store_name_list(self, num):
        store_name_instance = StoreNameGenerator()
        store_name_instance.store_place_list = FileReader().file_to_list("store_places.txt")

        # store_name_dic_list = [{"store_type":"", "store_name":""}, ... ,{"store_type":"", "store_name":""}]을 반환 받게 된다.
        store_name_dic_list = store_name_instance.generate_store_name_list(num)
        store_name_list = []
        store_type_list = []

        for store_name_dic in store_name_dic_list:
            store_name_list.append(store_name_dic['store_name'])
            store_type_list.append(store_name_dic['store_type'])

        return store_name_list, store_type_list

    def mk_store_address_list(self, num):
        address_instance = AddressGenerator()
        address_instance.korea_cities = FileReader().file_to_list("extra_files/korea_cities.txt")    
        address_instance.korea_gus = FileReader().file_to_list("extra_files/korea_gus.txt")      
        address_list = address_instance.generate_korea_address_list(num)

        return address_list

    def gen_info_by_type(self, num):
        individual_store_dic_list = []
        store_name_list = self.mk_store_name_list(num)
        store_address_list = self.mk_store_address_list(num)

        individual_store_dic = {
            "id" : None,
            "name" : None,
            "type" : None,
            "address" : None
        }       
        for i in range(1, num):
            individual_store_dic['id'] = self.mk_uuid(num)
            individual_store_dic['type'] = store_name_list[i]['store_type']
            individual_store_dic['name'] =  store_name_list[i]['store_name']
            individual_store_dic['address'] = store_address_list[i]

            individual_store_dic_list.append(individual_store_dic)

        return individual_store_dic_list