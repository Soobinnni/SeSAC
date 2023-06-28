from flask import Flask, url_for, render_template, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    users = []
    return render_template("hello3.html", users=users)

@app.route("/read-csv")
def read_csv():
    users = []
    with open("user.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            users.append(row)

    return render_template("hello3.html", user_info = users)

if __name__ == "__main__":
    app.run(debug=True)