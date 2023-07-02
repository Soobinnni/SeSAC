from flask import Flask, render_template, request

from paging import get_page_info

from service.user.user_service import UserService
from service.order.order_service import OrderService
from service.order_item.order_item_service import OrderItemService
from service.item.item_service import ItemService
from service.store.store_service import StoreService

app = Flask(__name__)

#services
user_service = UserService()
order_service = OrderService()
order_item_service = OrderItemService()
item_service = ItemService()
store_service = StoreService()

# ----------TODO : view도 폴더를 생성해서 그 안에 소속되게 하고 싶었지만, templates 때문에 보류..

# -------------------------------------------Home Start-----------------------------------------------------------------------
@app.route("/")
def home():
    response = render_template("home.html")
    return response
# -------------------------------------------Home End-----------------------------------------------------------------------

# -------------------------------------------User Start-----------------------------------------------------------------------
@app.route("/user/board/list")
def user_board_list():
    #log
    print('----------------------------view-user : @app.route("/user/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", default="no search", type=str)
    gender = request.args.get("gender", default="no search", type=str)

    # result
    result = []

    # 서비스 호출 나누기
    if( name == 'no search' and gender == 'no search' ):
        result = user_service.read_all()
    elif (len(name) != 0) and (len(gender) != 0) : 
        result = user_service.read_name_gender(name, gender)


    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("user/board/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num, name=name, gender=gender)
    return response


@app.route("/user/board/detail")
def user_board_detail():
    #log
    print('----------------------------view-user : @app.route("/user/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = user_service.read_id(id)

    #응답
    response = render_template("user/board/detail.html", data = data)
    return response

# -------------------------------------------User End-----------------------------------------------------------------------

# -------------------------------------------Order Start-----------------------------------------------------------------------
@app.route("/order/board/list")
def order_board_list():
    #log
    print('----------------------------view-order : @app.route("/order/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)

    # result
    result = []
    result = order_service.read_all()

    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("order/board/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num)
    return response


@app.route("/order/board/detail")
def order_board_detail():
    #log
    print('----------------------------view-order : @app.route("/order/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = order_service.read_id(id)

    #응답
    response = render_template("order/board/detail.html", data = data)
    return response

# -------------------------------------------Order End-----------------------------------------------------------------------
# -------------------------------------------Order Item Start---------------------------------------------------------------------
@app.route("/order-item/board/list")
def order_item_board_list():
    #log
    print('----------------------------view-order-item : @app.route("/order-item/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)

    # result
    result = []
    result = order_item_service.read_all()   
    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("order_item/board/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num)
    return response


@app.route("/order-item/board/detail")
def order_item_board_detail():
    #log
    print('----------------------------view-order-item : @app.route("/order-item/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = order_item_service.read_id(id)

    #응답
    response = render_template("order_item/board/detail.html", data = data)
    return response
# -------------------------------------------Order Item End-----------------------------------------------------------------------
# -------------------------------------------Item Start---------------------------------------------------------------------
@app.route("/item/board/list")
def item_board_list():
    #log
    print('----------------------------view-item : @app.route("/item/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    
    # result
    result = []
    result = item_service.read_all()
    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("item/board/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num)
    return response


@app.route("/item/board/detail")
def item_board_detail():
    #log
    print('----------------------------view-item : @app.route("/item/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = item_service.read_id(id)

    #응답
    response = render_template("item/board/detail.html", data = data)
    return response
# -------------------------------------------Item End-----------------------------------------------------------------------
# -------------------------------------------Store Start---------------------------------------------------------------------
@app.route("/store/board/list")
def store_board_list():
    #log
    print('----------------------------view-store : @app.route("/store/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
  
    # result
    result = []
    result = store_service.read_all()
    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("store/board/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num)
    return response


@app.route("/store/board/detail")
def store_board_detail():
    #log
    print('----------------------------view-store : @app.route("/store/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = store_service.read_id(id)

    #응답
    response = render_template("store/board/detail.html", data = data)
    return response
# -------------------------------------------Store End-----------------------------------------------------------------------
# ---------------------------------------------------------Main---------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5003)