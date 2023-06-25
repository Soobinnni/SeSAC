import csv
class Printer:
    def __init__(self):
        self.data_list = []
        self.print_type = ""
        self.file_name =""

    def print_by_console(self, data_list):
        # 콘솔창 출력 함수 
        for d in data_list:
            print(d.values())
        return False

    def print_by_csv(self, file_name, data_list):
        # 콘솔창 출력 함수 
        # csv 출력 함수
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for d in data_list:
                    writer.writerow(d.values())
        return False

    def print_output(self, data_list, file_name):
        incorrect_input = True
        while incorrect_input:
            output_type = input('\n<출력 방식을 선택하세요>\nconsole\ncsv\n\n입력 : ')
            if output_type == 'console':
                incorrect_input = self.print_by_console(data_list)
            elif output_type == 'csv':
                incorrect_input = self.print_by_csv(file_name, data_list)
            else:
                print('올바른 선택지를 입력하세요.')
                continue