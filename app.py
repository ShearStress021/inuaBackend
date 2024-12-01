from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route("/api/users", methods=["GET"])
def home():
    return jsonify({"users": ["obama", "Gracee", "Mary"]})


if __name__ == "__main__":
    app.run()
