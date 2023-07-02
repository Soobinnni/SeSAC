from flask import Blueprint, Flask, render_template, request

from paging import get_page_info
from service.user_service import UserService

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_service = UserService()

@user_bp.route("/board/list")
def user_board_list():
    #log
    print('----------------------------view-user : @user_bp.route("/user/board/list")')
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


@user_bp.route("/board/detail")
def user_board_detail():
    #log
    print('----------------------------view-user : @user_bp.route("/user/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = user_service.read_id(id)

    #응답
    response = render_template("user/board/detail.html", data = data)
    return response