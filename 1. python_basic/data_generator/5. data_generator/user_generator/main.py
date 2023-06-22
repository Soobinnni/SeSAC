from user_generator import UserInfoGenerator

def main():
    user_info_generator = UserInfoGenerator()
    # 출력할 정보 개수 입력
    data_num = user_info_generator.input_data_num()
    # 랜덤 정보 개수만큼 생성
    individual_info_list =user_info_generator.mk_individual_info(data_num)
    # 출력
    file_name = "user.csv"
    user_info_generator.print_output(individual_info_list, file_name)


if __name__ == "__main__":
    main()