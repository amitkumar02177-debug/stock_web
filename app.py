from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = "stocks.json"


@app.route("/")
def home():

    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            products = json.load(f)
    else:
        products = []

    return render_template("index.html", products=products)


@app.route("/update-stock", methods=["POST"])
def update_stock():

    data = request.get_json()

    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

    return jsonify({"status": "success"})

