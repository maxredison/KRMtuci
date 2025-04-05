from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Simple API!"


@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify(
            {"error": "Please provide both 'a' and 'b' parameters"}
        ), 400
    return jsonify({"result": a + b})


@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify(
            {"error": "Please provide both 'a' and 'b' parameters"}
        ), 400
    return jsonify({"result": a - b})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
