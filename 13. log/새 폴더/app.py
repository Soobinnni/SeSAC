from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    
    return """<h1>
                안녕하세요
            </h1>"""
# ---------------------------------------------views-----------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")