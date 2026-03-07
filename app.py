from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Absolute path to JSON file
DATA_FILE = os.path.join(os.path.dirname(__file__), "stocks.json")

# Home route: render the stock table
@app.route("/")
def home():
    last_update = "N/A"
    products = []

    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                content = f.read().strip()
                payload = json.loads(content) if content else {}
                products = payload.get("products", [])
                last_update = payload.get("last_update", "N/A")
    except Exception as e:
        print("Error reading JSON:", e)
        products = []
        last_update = "N/A"

    return render_template("index.html", products=products, last_update=last_update)
# Endpoint to update stock from your script
@app.route("/update-stock", methods=["POST"])
def update_stock():
    data = request.json
    # Wrap with timestamp
    payload = {
        "last_update": datetime.now().strftime("%d %b %Y %H:%M:%S"),
        "products": data
    }

    with open(DATA_FILE, "w") as f:
        json.dump(payload, f)

    return jsonify({"status": "success"})

if __name__ == "__main__":
    # Railway sets PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

