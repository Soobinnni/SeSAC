from user.user_generator import UserGenerator
from store.store_generator import StoreGenerator
from common.printer import Printer

def mk_user_info():
    user_generator = UserGenerator()
    # 출력할 정보 개수 입력
    data_num = user_generator.input_data_num()
    data_list = [
        {
            "id" : "Id",
            "name":"Name",
            "gender" :"Gender",
            "birthdate":"Birthdate",
            "age" : "Age",
            "address" : "Address"
        }
    ]
    # 랜덤 정보 개수만큼 생성
    individual_info_list = user_generator.generate(data_num, data_list)
    # 출력
    file_name = "user.csv"
    Printer().print_output(individual_info_list, file_name)

def mk_store_info():
    store_generator = StoreGenerator()
    # 출력할 정보 개수 입력
    data_num = store_generator.input_data_num()    
    data_list = [
        {
            "id" : "Id",
            "name":"Name",
            "type" :"Type",
            "address" : "Address"
        }
    ]
    # 랜덤 정보 개수만큼 생성
    store_info_list = store_generator.gen_info_by_type(data_num)
    # 출력
    file_name = "store.csv"
    Printer().print_output(store_info_list, file_name)

def main():
    mk_user_info()
    # mk_store_info()

if __name__ == "__main__":
    main()