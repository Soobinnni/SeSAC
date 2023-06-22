from  import Generator

from address_generator import AddressGenerator
from age_generator import AgeGenerator
from birthdate_generator import BirthdateGenerator
from gender_generator import GenderGenerator
from name_generator import NameGenerator

class UserInfoGenerator(Generator):
    def mk_name(self):
        name_instance = NameGenerator()
        name_instance.korean_first_names = self.file_to_list("korean_first_names.txt")
        name_instance.korean_last_names = self.file_to_list("korean_last_names.txt")  
        name = name_instance.generate_korean_name()

        return name

    def mk_gender(self):
        gender_instance = GenderGenerator()
        gender = gender_instance.generate_gender()

        return gender

    def mk_birthdate(self):
        birthdate_instance = BirthdateGenerator()
        birthdate = birthdate_instance.generate_birthdate()

        return birthdate

    def mk_age(self, birthdate):
        age_instance = AgeGenerator()
        age_instance.birthdate_year = int(birthdate[0:4])
        age = age_instance.get_age()

        return age


    def mk_address(self):
        address_instance = AddressGenerator()
        address_instance.korea_cities = self.file_to_list("korea_cities.txt")    
        address_instance.korea_gus = self.file_to_list("korea_gus.txt")      
        address = address_instance.generate_korea_address()

        return address

    def generate_individual_info(self):
        individual_info_dic = {
            "name" : None,
            "gender" : None,
            "birthdate" : None,
            "age" : None,
            "address" : None
        }       
        individual_info_dic['name'] = self.mk_name()
        individual_info_dic['gender'] = self.mk_gender()
        birthdate = self.mk_birthdate()
        individual_info_dic['birthdate'] = birthdate
        individual_info_dic['age'] = self.mk_age(birthdate)
        individual_info_dic['address'] = self.mk_address()

        return individual_info_dic
    
