from address_generator import AddressGenerator
from age_generator import AgeGenerator
from birthdate_generator import BirthdateGenerator
from gender_generator import GenderGenerator
from name_generator import NameGenerator


def generate_individual_info():
    names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']

    name_instance = NameGenerator(names)
    address_instance = AddressGenerator(cities)
    gender_instance = GenderGenerator()
    birth_instance = BirthdateGenerator()
    age_instance = AgeGenerator()

    name = name_instance.generate_name()
    gender = gender_instance.generate_gender()
    birth = birth_instance.generate_birthdate()
    address = address_instance.generate_address()

    age_instance.birthdate_year = int(birth[0:4])
    age = age_instance.get_age()
    
    individual_info = (name, gender, birth, age, address)
    result = ', '.join(str(value) for value in individual_info)
    return result


def main():
    data_list = []

    print('Name, Birthdate, Gender, Address')
    for _ in range(10):
        data_list.append(generate_individual_info())

    for d in data_list:
        print(d)


if __name__ == "__main__":
    main()