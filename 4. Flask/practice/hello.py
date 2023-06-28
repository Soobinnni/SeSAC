from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #template 사용법 : templates/폴더 경로 이후의 경로를 적으면 됨
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)