from flask import Flask, url_for, render_template, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    user_list = []
    with open('user.csv', 'r', encoding="utf-8") as file:
        csv_data = csv.DictReader(file)
        for data in csv_data:
                user_list.append(data) 
    print(user_list)
    return render_template("main.html", data= user_list)

@app.route("/user/detail/<user_id>")
def user_detail(user_id):
    user_info = None
    # DB가 아직 없으니까 파일에서 정보 찾기
    with open("user.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if user_id in row :
                user_info = row
    return render_template("user/detail.html", user_info = user_info)

@app.route("/index")
def index():
    # 한 페이지에 담길 컨텐츠 수를 정한다.(num)
    per_page = 10
    total_pages = None
    start_index = None
    
    data = []
    with open('data_space.csv', 'r', encoding="utf-8") as file:
        csv_data = csv.DictReader(file)
        headers = [header.strip() for header in csv_data.fieldnames]
        
        for row in csv_data:
            clean_row = {key.strip() : value.strip() for key, value in row.items()}
            data.append(clean_row) 
        
    return render_template("main.html", data = data)

if __name__ == "__main__":
    app.run(debug=True, port=5002)