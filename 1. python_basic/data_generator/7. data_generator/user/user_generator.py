from common.generator import Generator

from common.address_generator import AddressGenerator
from user.age_generator import AgeGenerator
from user.birthdate_generator import BirthdateGenerator
from user.gender_generator import GenderGenerator
from user.name_generator import NameGenerator
from common.file_reader import FileReader

class UserGenerator(Generator):
    def __init__(self):
        self.name_instance = NameGenerator()
        self.gender_instance = GenderGenerator()
        self.birthdate_instance = BirthdateGenerator()
        self.age_instance = AgeGenerator()
        self.address_instance = AddressGenerator()

    def mk_name(self):
        self.name_instance.korean_first_names = FileReader().file_to_list("korean_first_names.txt")
        self.name_instance.korean_last_names = FileReader().file_to_list("korean_last_names.txt")  
        name = self.name_instance.generate_korean_name()

        return name

    def mk_gender(self):
        gender = self.gender_instance.generate_gender()

        return gender

    def mk_birthdate(self):
        birthdate = self.birthdate_instance.generate_birthdate()

        return birthdate

    def mk_age(self, birthdate):
        self.age_instance.birthdate_year = int(birthdate[0:4])
        age = self.age_instance.get_age()

        return age


    def mk_address(self):
        self.address_instance.korea_cities = FileReader().file_to_list("korea_cities.txt")    
        self.address_instance.korea_gus = FileReader().file_to_list("korea_gus.txt")      
        address = self.address_instance.generate_korea_address()

        return address

    def gen_info_by_type(self):
        individual_info_dic = {
            "id" : None,
            "name" : None,
            "gender" : None,
            "birthdate" : None,
            "age" : None,
            "address" : None
        }       

        individual_info_dic['id'] = self.mk_uuid()
        individual_info_dic['name'] = self.mk_name()
        individual_info_dic['gender'] = self.mk_gender()
        # birthdate
        individual_info_dic['birthdate'] = birthdate = self.mk_birthdate()
        individual_info_dic['age'] = self.mk_age(birthdate)
        individual_info_dic['address'] = self.mk_address()

        return individual_info_dic