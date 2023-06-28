from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    username = ['kim', 'lee', 'jung']
    return  render_template("index2.html", username = username)

if __name__ == "__main__" :
    app.run(debug=True)