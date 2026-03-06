from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "stock.json"

@app.route("/")
def home():

    if not os.path.exists(DATA_FILE):
        products = []
    else:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()

            if content == "":
                products = []
            else:
                products = json.loads(content)

    return render_template("index.html", products=products)
