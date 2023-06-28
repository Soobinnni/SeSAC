from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route("/<aaa>")
def home(aaa):

    return aaa

@app.route("/test_url")
def test():
    return render_template("index2.html", asdf="아무거나")

if __name__ == "__main__":
    app.run(debug=True)