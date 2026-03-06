from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = "stock.json"


def load_stock():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_stock(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


@app.route("/")
def home():
    stock = load_stock()
    return render_template("index.html", stock=stock)


@app.route("/update_stock", methods=["POST"])
def update_stock():
    data = request.json
    save_stock(data)
    return {"status": "success"}


if __name__ == "__main__":
    app.run()