from flask import Flask, url_for, render_template, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    users = []
    return render_template("hello3.html", users=users)

@app.route("/read-user")
def read_csv():
    user_list = []
    with open("user.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            user_list.append(row)

    return render_template("hello3.html", user_info = user_list)

@app.route("/user/detail/<user_id>")
def user_detail(user_id):
    user_info = None
    # DB가 아직 없으니까 파일에서 정보 찾기
    with open("user.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if user_id in row :
                user_info = row
    return render_template("detail.html", user_info = user_info)


if __name__ == "__main__":
    app.run(debug=True, port=5001)