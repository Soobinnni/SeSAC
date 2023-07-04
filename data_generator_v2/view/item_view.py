from flask import Blueprint, Flask, render_template, request

from view.paging_view import get_page_info
from service.item_service import ItemService
from domain.item import Item

item_bp = Blueprint('item', __name__, url_prefix='/item')
item_service = ItemService()

@item_bp.route("/board/list")
def item_board_list():
    #log
    print('----------------------------view-item : @item_bp.route("/item/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", type=str, default="no search")
    unit_price = request.args.get("unit_price", type=int, default=-1)

    # result
    result = []
    if (name == 'no search') and (unit_price == -1):
        result = item_service.read_all()
    elif (len(name) !=0) and ( unit_price == -1) :
        result = item_service.read_name(name)
    elif (len(name) !=0) and ( unit_price != -1) :
        result = item_service.read_name_price(name, unit_price)

    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("item/board/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num, name=name, unit_price = unit_price)
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

# --------------------------------------------------------register-----------------------------------------------------------------
@item_bp.route("/register", methods = ['GET', 'POST'])
def item_register():
    response = None
    if request.method == 'GET' :
        #log
        print('----------------------------view-item : @item_bp.route("/register", methods = ["GET"])')
        #응답
        response = render_template("item/register.html")

    elif request.method == 'POST' :
        #log
        print('----------------------------view-item : @item_bp.route("/register", methods = ["POST"])')
        
        # form value
        name =  request.form['name']
        type_ =  request.form['type']
        unit_price =  request.form['unit_price']

        # mk name ex: Americano Coffee
        name = name + " " +type_

        # item domain init
        item = Item(name, type_, unit_price)

        # item create service
        item_service.create(item)

        #응답
        response = render_template("item/register.html")

    return response