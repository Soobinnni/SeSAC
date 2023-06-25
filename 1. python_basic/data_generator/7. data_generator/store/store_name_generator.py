import random


class StoreNameGenerator:
    def __init__(self):
        self.store_type = None
        self.store_place_list = None

    def generate_store_type_list(self, num):
        store_type_list = random.choices(self.store_type_list, k=num)  
        store_name_list = []
        store_name_dic = {
            "store_type" : "",
            "store_name" : ""
        } 

        for store_type in store_type_list:
            store_name_dic['store_type'] = store_type
            store_name_list.append(store_name_dic)

        return store_name_list
    
    def generate_store_name_list(self, num):
        store_name_list = self.generate_store_type_list(self, num)
        store_place_list = random.choices(self.store_place_list, k=num)

        for i, store_name in enumerate(store_name_list):
            store_type = store_name[i]['store_type']
            store_place = store_place_list[i]

            store_name = store_type + ' ' + store_place + str(random.randint(1,10)) + '호점'

            store_name['store_name'] = store_name

        return store_name_list
    
