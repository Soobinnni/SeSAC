from flask import Blueprint, Flask, render_template, request

from view.paging import get_page_info
from service.item_service import ItemService

item_bp = Blueprint('item', __name__, url_prefix='/item')
item_service = ItemService()

@item_bp.route("/board/list")
def item_board_list():
    #log
    print('----------------------------view-item : @item_bp.route("/item/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    
    # result
    result = []
    result = item_service.read_all()
    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("item/board/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num)
    return response


@item_bp.route("/board/detail")
def item_board_detail():
    #log
    print('----------------------------view-item : @item_bp.route("/item/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = item_service.read_id(id)

    #응답
    response = render_template("item/board/detail.html", data = data)
    return response