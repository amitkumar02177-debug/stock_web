from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "stock.json"


@app.route("/")
def home():

    last_update = datetime.now().strftime("%d %b %Y %H:%M:%S")

    if not os.path.exists(DATA_FILE):
        products = []
    else:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()

            if content == "":
                products = []
            else:
                products = json.loads(content)

    return render_template("index.html", products=products, last_update=last_update)


@app.route("/update-stock", methods=["POST"])
def update_stock():

    data = request.json

    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run()
