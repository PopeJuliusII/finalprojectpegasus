from flask import Flask, jsonify, request
from flask_cors import CORS
from os import path
from db_interaction import ORM, Saved, Users, Preferences

app = Flask(__name__)
CORS(app)

PATH = path.join(path.split(path.abspath(path.dirname(__file__)))[0], 'data', 'database', 'pegasus.db')
ORM.dbpath = PATH


@app.route('/get_data/<id>/<email>', methods=["GET"])
def get_data(id, email):
    try:
        pk = Users.find_one('id', id).pk
    except TypeError:
        Users(id=id, email=email).insert()
        pk = Users.find_one('id', id).pk
    prefs, saved = None, None
    try:
        prefs = Preferences.find_all('userid', pk)
    except TypeError:
        if not prefs:
            Preferences(userid=pk, vegetarian=0, italian=0, kosher=0).insert()
    try:
        saved = Saved.find_all('userid', pk)
    except TypeError:
        saved = None
    return jsonify({f'data{pk}': {'saved': saved, 'prefs': prefs}})


@app.route('/add_saved/', methods=["GET", "POST"])
def add_saved():
    data = request.get_json()
    new_entry = Saved(userid=1)
    return jsonify({'message': 'success'})


@app.route('/add_preferences/', methods=["GET", "POST"])
def add_preferences():
    return jsonify({'message': 'success'})


@app.route('/post_location/', methods=["POST"])
def add_trip():
    return jsonify({'data': f'{id}:{email}'})


@app.route('/get_recommendation/', methods=["POST"])
def get_rec():
    return jsonify({'data': f'{id}:{email}'})


if __name__ == "__main__":
    app.run(debug=True)
