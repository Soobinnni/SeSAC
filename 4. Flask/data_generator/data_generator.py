from flask import Flask, url_for, render_template, redirect, request
import csv
import math

app = Flask(__name__)

@app.route("/")
def home():
    # 일단 홈의 내용을 넘기고, redirect
    response = redirect(url_for("user_board"))
    return response

@app.route("/user/board")
def user_board():
    # request객체를 이용하여 name에 대한 value를 얻을 수 있다. type과 default값을 지정할 수 있다.
    # request.args.get("keyname", type="datatype", default=default_value) -> default 생략가능
    search_result = None
    # parameter values
    page_num = request.args.get("page_num", type="int", default=1)
    name = request.args.get("name", default="", type="str")
    gender = request.args.get("gender", default="", type="str")

    datas = read_csv('data_space.csv')
    search_data = []
    if (len(name) != 0) and (len(gender) != 0) : 
        for data in datas:
            for value in data.values():
                if name in value :
                    search_data.append(value)
            

    total_page, page_datas = get_page_info(page_num, datas)

    return render_template("user/borad/page.html",datas=datas, total_page=total_page,page_datas=page_datas,page_num=page_num, name=name, gender=gender)

def read_csv(file_name) :
    datas =[]    
    #read data from csv file
    with open(file_name,'r',encoding='utf-8') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            clean_row = {key.strip() : value.strip() for key, value in row.items()}
            datas.append(clean_row) 
    #return type-> dic을 담은 list
    return datas

def get_page_info(page_num, datas):
    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1

    # ceil 함수는 실수를 입력하면 올림 하여 정수를 반환하는 함수이다.
    total_page=math.ceil(len(datas)/per_page)
    
    # 0~9 / 10~19 / 20~29
    start_index=(page_num-1)*page_num
    # 슬라이싱은 마지막 범위가 미만이니까 
    end_index=page_num*per_page
    print(f"page_num{page_num} : {start_index},{end_index}")

    page_datas=datas[start_index:end_index] 

    return (total_page, page_datas)

if __name__ == "__main__":
    app.run(debug=True, port=5002)

    