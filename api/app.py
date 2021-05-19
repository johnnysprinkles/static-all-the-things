from flask import Flask, jsonify
from data import data
from flask_cors import CORS
import time

ARTIFICIAL_DELAY = 0.5 # seconds

app = Flask(__name__)
CORS(app)

@app.route("/list")
def list():
    time.sleep(ARTIFICIAL_DELAY)
    return jsonify(data)

@app.route("/detail/<id>")
def get(id):
    time.sleep(ARTIFICIAL_DELAY)
    id = int(id)
    matches = [x for x in data if x["id"] == id]
    if len(matches) > 0:
        return matches[0]
    else:
        return jsonify([]), 404

if __name__ == '__main__':
    app.run(host="localhost", port=3001)