from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "stocks.json"

@app.route("/")
def home():
    if not os.path.exists(DATA_FILE):
        products = []
        last_update = "N/A"
    else:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            products = json.loads(content) if content else []
            last_update = datetime.now().strftime("%d %b %Y %H:%M:%S")
    return render_template("index.html", products=products, last_update=last_update)

@app.route("/update-stock", methods=["POST"])
def update_stock():
    data = request.json
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    # Railway sets the port in environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
