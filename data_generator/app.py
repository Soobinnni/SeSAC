from flask import Flask, render_template

from view.user_view import user_bp
from view.item_view import item_bp
from view.order_view import order_bp
from view.order_item_view import order_item_bp
from view.store_view import store_bp

app = Flask(__name__)
# -------------------------------------------Home-----------------------------------------------------------------------
@app.route("/")
def home():
    response = render_template("home.html")
    return response
# -------------------------------------------Other views-----------------------------------------------------------------
app.register_blueprint(user_bp)
app.register_blueprint(item_bp)
app.register_blueprint(order_bp)
app.register_blueprint(order_item_bp)
app.register_blueprint(store_bp)
# ---------------------------------------------------------Main-----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5003)