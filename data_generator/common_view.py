from flask import Flask, url_for, render_template, redirect, request
import csv
import math
from service.user.user_service import UserService
from service.order.order_service import OrderService

app = Flask(__name__)
user_service = UserService()
order_service = OrderService()
# ----------view도 폴더를 생성해서 그 안에 소속되게 하고 싶었지만, templates 때문에 보류..

# -------------------------------------------Home Start-----------------------------------------------------------------------
@app.route("/")
def home():
    # 일단 redirect
    response = redirect(url_for("user_board_list"))
    return response
# -------------------------------------------Home End-----------------------------------------------------------------------

# -------------------------------------------User Start-----------------------------------------------------------------------
@app.route("/user/board/list")
def user_board_list():
    #log
    print('----------------------------view : @app.route("/user/board/list")')
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

    total_page, page_datas = get_page_info(page_num, result)

    response = render_template("user/board/list.html", datas=result, total_page=total_page, page_datas=page_datas, page_num=page_num, name=name, gender=gender)
    return response


@app.route("/user/board/detail")
def user_board_detail():
    #log
    print('----------------------------view : @app.route("/user/board/detail")')
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
    print('----------------------------view : @app.route("/order/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    # name = request.args.get("name", default="no search", type=str)
    # gender = request.args.get("gender", default="no search", type=str)

    # result
    result = []
    result = order_service.read_all()
    # 서비스 호출 나누기
    # if( name == 'no search' and gender == 'no search' ):
    #     result = user_service.read_all()
    # elif (len(name) != 0) and (len(gender) != 0) : 
    #     result = user_service.read_name_gender(name, gender)

    total_page, page_datas = get_page_info(page_num, result)

    # response = render_template("order/board/list.html", datas=result, total_page=total_page, page_datas=page_datas, page_num=page_num, name=name, gender=gender)
    response = render_template("order/board/list.html", datas=result, total_page=total_page, page_datas=page_datas, page_num=page_num)
    return response


@app.route("/order/board/detail")
def order_board_detail():
    #log
    print('----------------------------view : @app.route("/order/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = user_service.read_id(id)

    #응답
    response = render_template("user/board/detail.html", data = data)
    return response

# -------------------------------------------Order End-----------------------------------------------------------------------

# -------------------------------------------Etc Start-----------------------------------------------------------------------
def get_page_info(page_num, datas):
    #log
    print('----------------------------view : get_page_info')

    per_page=10
    total_page=-1
    start_index=-1
    end_index=-1

    if datas != 0 :
        # ceil 함수는 실수를 입력하면 올림 하여 정수를 반환하는 함수이다.
        total_page=math.ceil(len(datas)/per_page)
        
        # 0~9 / 10~19 / 20~29
        start_index=(page_num-1)*per_page
        # 슬라이싱은 마지막 범위가 미만이니까 
        end_index=page_num*per_page
        print(f"page_num{page_num} : {start_index},{end_index}")

        page_datas=datas[start_index:end_index] 

    return (total_page, page_datas)
# -------------------------------------------Etc End-----------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5003)
