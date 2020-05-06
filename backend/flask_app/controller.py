from flask import Flask, jsonify, request
from flask_cors import CORS
from os import path
from db_interaction import ORM, Saved, Users, Preferences
from sqlite3 import IntegrityError

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
        pk = int(Users.find_one('id', id).pk)
    prefs, saved = None, None
    try:
        prefs = Preferences.find_one('userid', pk)
    except TypeError:
        Preferences(userid=pk, vegetarian=0, italian=0, kosher=0).insert()
    prefs = Preferences.find_one('userid', pk)
    saved = Saved.find_all('userid', pk)
    return jsonify({f'data':
                    {'saved': {k: v for k, v in saved.__dict__.items() if k not in ['pk', 'userid']} if saved else None,
                     'prefs': {k: v for k, v in prefs.__dict__.items() if k not in ['pk', 'userid']}}})


@app.route('/add_saved', methods=["GET", "POST"])
def add_saved():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({'message': 'Log in or sign up.'})
    pk = Users.find_one('id', data.get('id')).pk
    name, category = data.get('name'), data.get('category')
    address, latitude, longitude = data.get('address'), data.get('latitude'), data.get('longitude')
    new_entry = Saved(userid=pk, name=name, category=category, address=address, latitude=latitude, longitude=longitude)
    try:
        new_entry.insert()
    except IntegrityError:
        pass
    return jsonify({'data': {k: v for k, v in new_entry.__dict__.items() if k not in ['pk', 'userid']}})


@app.route('/del_saved', methods=["GET", "POST"])
def del_saved():
    data = request.get_json()
    pk = Users.find_one('id', data.get('id')).pk
    Saved(userid=pk, name=data.get('name')).delete('userid', pk, 'name', data.get('name'))
    return jsonify({'message': 'success'})


@app.route('/add_preferences', methods=["GET", "POST"])
def add_preferences():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({'message': 'Log in or sign up.'})
    pk = Users.find_one('id', data.get('id')).pk
    vegetarian, italian, kosher = data.get('vegetarian'), data.get('italian'), data.get('kosher')
    Preferences(userid=pk, vegetarian=vegetarian, italian=italian, kosher=kosher).update('userid', pk)
    return jsonify({'data': 'success'})


@app.route('/get_recommendation', methods=["POST"])
def get_rec():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({'message': 'Log in or sign up.'})
    pk = Users.find_one('id', id).pk
    return {'data': f'{pk}'}

    # check if near station
    # if yes:
    # check if most recent trip was less than five minutes hence
    # if yes:
    # update entry
    # if no:
    # new entry
    # save to trips
    # get prefs
    # send recommendations
    # if no:
    # return nothing.
    return jsonify({'data': ''})


if __name__ == "__main__":
    app.run(debug=True)
