import csv

class Generator:
    def file_to_list(self, file_name):
        result = None
        with open(file_name, "r", encoding='utf-8') as file: #mode - r(read), w(write), a(append)
            result =  file.read().split(', ')
        return result

    def input_data_num(self):
        incorrect_input = True
        data_num = None
        while incorrect_input:
            try:
                data_num = int(input('<생성할 정보의 개수를 입력하세요 >\n입력 : '))
                incorrect_input = False
            except ValueError:
                print('숫자를 입력해주세요. \n')
                continue
        return data_num

    # TODO : 함수 고치기(list받기)
    def mk_individual_info(self, num):
        data_list = [
            {
                "name":"Name",
                "gender" :"Gender",
                "birthdate":"Birthdate",
                "age" : "Age",
                "address" : "Address"
            }
        ]
        for _ in range((num)):
            data_list.append(self.generate_individual_info()) 

        return data_list

    def print_output(self, data_list, file_name):
        incorrect_input = True
        while incorrect_input:
            output_type = input('\n<출력 방식을 선택하세요>\nconsole\ncsv\n\n입력 : ')
            if output_type == 'console':
                # 콘솔창 출력 함수 
                for d in data_list:
                    print(d.values())
                incorrect_input = False
            elif output_type == 'csv':
                # csv 출력 함수
                with open(file_name, "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    for d in data_list:
                            writer.writerow(d.values())
                    incorrect_input = False
            else:
                print('옳바른 선택지를 입력하세요.')
                continue
