from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get_data/<id>/<email>', methods=["GET"])
def get_data(id, email):
    return jsonify({'data': f'{id}:{email}'})


@app.route('/add_saved/', methods=["GET", "POST"])
def add_saved():
    return jsonify({'message': 'success'})


@app.route('/add_preferences/', methods=["GET", "POST"])
def add_preferences():
    return jsonify({'message': 'success'})


@app.route('/post_location/', methods=["POST"])
def add_trip():
    return jsonify({'data': f'{id}:{email}'})


@app.route('/get_recommendation/', methods=["POST"])
def add_trip():
    return jsonify({'data': f'{id}:{email}'})


if __name__ == "__main__":
    app.run(debug=True)
