from flask import Flask, render_template, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# 상품 정보 등록
items = {
    'item1' : {'name' : '상품1', 'price' : 1000 },
    'item2' : {'name' : '상품2', 'price' : 2000 },
    'item3' : {'name' : '상품3', 'price' : 3000 }
}
def get_item_sq_price(item_name) :
    item_sq = ""
    item_price = 0
    for key, value in items.items() :
        if value['name'] == item_name:
            item_sq = key
            item_price = value['price']

    return item_sq, item_price

@app.route("/")
def index():
    return render_template("index.html", items = items)

@app.route("/add-to-cart/<item_name>")
def add_to_cart(item_name) :
    item_sq, item_price = get_item_sq_price(item_name)

    if 'cart' not in session : # if session['cart'] 는 session['cart']의 초기화가 된 적이 없기 때문에 문법적 오류가 발생
        session['cart'] = {}

    # 카트에 물건 담기
    if item_sq in session['cart'] :
        count = session['cart'][item_sq]['count'] + 1 
        session['cart'][item_sq] = {'name' : item_name, 'price' : (item_price * count), 'count' : count}
    else :
        session['cart'][item_sq] = {'name' : item_name, 'price' : (item_price * 1), 'count' : 1}

    # 세션 데이터가 수정되었음을 Flask에 알림
    session.modified = True
    
    # print(session)
    # 담은 이후 액션
    return redirect(url_for('index'))

@app.route('/view-cart')
def view_cart() :
    response = render_template("view-cart.html", cart = False )
    if 'cart' in session :
        print(session['cart'])
        response = render_template("view-cart.html", cart = session['cart'] )
    
    return response

@app.route("/delete-item/<item_name>")
def delete_item(item_name) :
    response = ""
    item_sq, _ = get_item_sq_price(item_name)
    
    if 'cart' in session :
        if item_sq in session['cart'] :
            session['cart'].pop(item_sq)
            response = render_template("view-cart.html", cart = session['cart'] )

        if not session['cart'] :
            session.pop("cart", None)
            response = render_template("view-cart.html", cart = False)
    # 세션 데이터가 수정되었음을 Flask에 알림
    session.modified = True

    return response

if __name__ == '__main__':
    app.run(debug=True)