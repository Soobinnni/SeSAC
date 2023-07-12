import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

"""
    TODO : 월간 매출액 합산을 구하시오
    테이블로 2023-1, ... ,2023-12
    1. db에 접속한다.
    2.커서를 만든다.
    3.SQL문을 작성한다.
    4.쿼리문을 실행해서 결과를 받아온다(리스트 형태)
    5.랜더템플릿에 데이터를 전송한다.
"""

@app.route("/") 
def home() :
    conn = sqlite3.connect("crm.db")
    cursor = conn.cursor()
    sql = """
        SELECT SUBSTR(o.ordered_at, 1, 7), SUM(i.unit_price)
        FROM "order" o
        JOIN order_item oi ON o.id = oi.order_id
        JOIN item i ON i.id = oi.item_id
        GROUP BY SUBSTR(o.ordered_at, 1, 7)
    """
    datas = cursor.execute(sql).fetchall()
    conn.close()

    labels = []
    values = []
    for data in datas :
        label, value = data
        labels.append(label)
        values.append(value)


    response = render_template("index.html", datas = datas, labels = labels, values = values)
    return response

@app.route("/map") 
def map() :
    response = render_template("map.html")
    return response

if __name__ == "__main__" :
    app.run(debug=True)