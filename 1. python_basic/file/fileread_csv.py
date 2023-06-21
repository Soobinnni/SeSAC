# csv = comma seperated value (콤마로 구분된 파일)
# csv를 다루는 라이브러리 존재.
import csv

with open("user.csv", "r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)