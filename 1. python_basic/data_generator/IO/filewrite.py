data = "\nHello, world"

filepath = "1. python_basic\data_generator\IO\\"
filename = "myfile.txt"

# with open("names.txt", "w") as file:
with open(filepath + filename, "a") as file:
    file.write(data)

print('파일 쓰기 완료!')
