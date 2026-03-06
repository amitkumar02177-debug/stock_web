from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Stock server running"

@app.route("/update-stock", methods=["POST"])
def update_stock():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"status": "success"})
