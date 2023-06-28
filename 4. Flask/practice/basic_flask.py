from flask import Flask, url_for, redirect, render_template, request

# 인자 -> 고유식별자 필요 (__name__은 파일 이름)
app = Flask(__name__)

# /
@app.route('/')
def home():
    return 'Hello SeSAC!> <a href="/form">로그인으로 이동</a>'

# ------------------------path 실습---------------------------------
# /users
@app.route('/users')
def users():
    return '<li><a href="/user/kim">김</a></li><li><a href="/user/lee">이</a></li><li><a href="/user/jung">정</a></li>'




# /user/변수
@app.route('/user/<name1>')
def user_path(name2):
    return f'{name2}'

# ------------------------name과 value 실습--------------------------------
# /form
@app.route('/form')
def form():
    return '''\
    <!DOCTYPE html>
<html lang="ko"> 
<head>
    <meta charset="utf-8">
    <title>
        로그인 폼
    </title>
</head>
<body>
    <form action="/user/name" method="get" >
        <label for="name">이름</label> : <input name="name" type="text" id="name"/>
        <input type='submit' value='제출' />
    </form>
</body>
</html>\
    '''
# /user/name
@app.route('/user/name?name=<name>')
def user(name):
    return f'{name}'


# ------------------------redirect실습--------------------------------
# Flask모듈의 url_for, redirect를 활용


# `redirect` 함수는 Flask 웹 프레임워크에서 제공하는 함수로, 클라이언트를 다른 URL로 리디렉션(redirect)시키는 데 사용됩니다. 
# 즉, 사용자가 접근한 URL을 다른 URL로 자동으로 이동시키는 역할을 합니다.

# `redirect` 함수는 `url_for` 함수와 함께 사용되는 것이 일반적입니다. 
# `url_for` 함수는 Flask 애플리케이션에서 정의한 라우트 함수에 대한 URL을 생성해주는 함수입니다. 
# 이 함수는 라우트 함수의 이름과 필요한 매개변수를 인자로 받아서 해당 라우트 함수에 대한 URL을 생성합니다.

# 예를 들어, 위의 코드에서 `redirect(url_for('user', name="admin"))`는 `user`라는 이름의 라우트 함수에 대한 URL을 생성하고, 
# 해당 URL로 리디렉션을 수행합니다. `name="admin"`은 `user` 함수의 `name` 매개변수에 "admin" 값을 전달하는 역할을 합니다.

# 따라서, `/admin` URL에 접근하면 `user` 함수로 리디렉션되며, `name` 매개변수에는 "admin" 값이 전달될 것입니다.

@app.route('/admin')
def admin():
    return redirect(url_for('user', name="admin"))

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')

    return render_template('greet.html', name=name)

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
    # app.run(port=5001)
    # app.run(debug=True, port=5001)