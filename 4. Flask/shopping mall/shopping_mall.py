from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home(user_info=""):
    print(user_info)
    if user_info == None :
        user_info =""
    response = render_template("shopping_mall/home.html", user_info = user_info)
    return response

# @app.route("/login", method="POST")
@app.route('/loginform')
def loginform():
    response = render_template("shopping_mall/login_form.html")
    return response

# @app.route("/login", method="POST")

@app.route('/login')
def login():
    # user_info = {
    #     "id" :request.form['id'], 
    #     "pwd" :request.form['pwd']
    # }
    user_info = {
        "id" :request.args["id"], 
        "pwd" :request.args["pwd"]
    }

    
    
    print(f"사용자 아이디 : {user_info['id']}\n사용자 비밀번호 : {user_info['pwd']}")
    # login 을 처리하는 경로. login 성공 시, home함수의 경로로 redirect
    move = redirect(url_for("home", user_info = user_info))

    return move

@app.route('/logout')
def logout():
    pass

if __name__ == "__main__" :
    app.run(debug=True)
    print("goodbye")