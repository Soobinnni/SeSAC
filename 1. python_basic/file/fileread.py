# as뒤의 file로 연 파일을 컨트롤(변수)
with open("names.txt", "r") as file: #mode - r(read), w(write), a(append)
    names = file.read()
    print(names)

with open("names.txt", "r") as file:
    lines = file.readlines() #한 줄 씩 읽음

for line in lines:
    print(line.strip()) #strip() : 공백 제거