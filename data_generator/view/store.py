from flask import Blueprint, Flask, render_template, request

from paging import get_page_info
from service.store_service import StoreService

store_bp = Blueprint('store', __name__, url_prefix='/store')
store_service = StoreService()

@store_bp.route("/board/list")
def store_board_list():
    #log
    print('----------------------------view-store : @store_bp.route("/store/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
  
    # result
    result = []
    result = store_service.read_all()
    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("store/board/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num)
    return response


@store_bp.route("/board/detail")
def store_board_detail():
    #log
    print('----------------------------view-store : @store_bp.route("/store/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = store_service.read_id(id)

    #응답
    response = render_template("store/board/detail.html", data = data)
    return response