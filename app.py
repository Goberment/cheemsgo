from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return jsonify({"succes": True, "message": "Helo world"}), 200


if __name__ == "__main__":
    app.run(port=5001)