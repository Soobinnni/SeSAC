import csv
import uuid

class Generator:
    # - M5. 생성하는 개수를 동적으로 입력받고, 원하는 출력 타입 (console, csv) 에 따라 결과물을 출력하시오.
    #   이름을 한국 이름으로 (성/이름), 그리고 주소도 한국 도로명 주소 형태로 생성하시오.
    #   객체지향 설계를 하여, 신규 타입이(상점 등) 추가 될때 확장성 있게 설계하시오. (상속을 통해 필수 generate 함수를 구현하도록..)     
    def mk_uuid(self) :
        id = uuid.uuid4()
        return id
    
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
                if data_num < 0 :
                    raise ValueError
                incorrect_input = False
            except ValueError:
                print('양수 / 숫자를 입력해주세요. \n')
                continue
        return data_num
    
    def generate_info(self) :
        pass

    def mk_info(self, num, data_list):
        for _ in range((num)):
            data_list.append(self.generate_info()) 

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
                print('올바른 선택지를 입력하세요.')
                continue
