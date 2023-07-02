from flask import Flask, render_template

from view.user import user_bp
from view.item import item_bp
from view.order import order_bp
from view.order_item import order_item_bp
from view.store import store_bp

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