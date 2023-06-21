# csv = comma seperated value (콤마로 구분된 파일)
# csv를 다루는 라이브러리 존재.
import csv

data = [
    ("name", "age", "city"),
    ("john", 25, "seoul"),
    ("bill", 20, "busan"),
    ("kim", 22, "seoul")
]

# 새로운 라인이 생길 때 어떻게 할 것인지 == newline으로 설정
with open("user.csv", "w", newline="") as file:
    csv_file = csv.writer(file)
    csv_file.writerows(data)

print('csv write done')