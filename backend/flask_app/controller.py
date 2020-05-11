from flask import Flask, jsonify, request
from flask_cors import CORS
from os import path
from db_interaction import ORM, Saved, Users, Preferences, TubeStations, Trips, PreferenceIds
from sqlite3 import IntegrityError
import requests

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
                    {'saved': [{k: v for k, v in place.__dict__.items()} for place in saved] if saved else None,
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


@app.route('/get_recommendation', methods=["GET", "POST"])
def get_recommendation():
    data = request.get_json()
    if not data.get('id'):
        return jsonify({'message': 'Log in or sign up.'})
    pk = Users.find_one('id', data.get('id')).pk
    lat, lon = float(data.get('lat')), float(data.get('lon'))
    station = TubeStations.find_closest(lat, lon)
    if not station:
        return jsonify({'message': 'too far to rec'})
    Trips.new_entry(station.stop_name, pk)
    # return {'data': f'{pk, lat, lon, station.stop_name}'}
    prefs = Preferences.find_one('userid', pk)
    prefs = {k: v for k, v in prefs.__dict__.items() if k not in ['pk', 'userid']}
    query = []
    for key in prefs.keys():
        if prefs[key] == 1:
            fs_id = PreferenceIds.get_id(key)
            query.append(fs_id[0]) if fs_id else None
    print(query)
    cats = '&categoryId=' + ','.join(query) if query else None
    print(cats)
    response = requests.get(f"https://api.foursquare.com/v2/venues/search?&client_id=SPJKIIRUO1MO0VEZQ4YC1VBIGUVJ3IBVYQIS5MWLRO0D53K0&client_secret=JAISUVIQTX44KNXZ0N2FOMJ1FCKARINB5OCFLJWQ1XVAU42V&ll={lat},{lon}&v=20200404&limit=50&radius=100{cats}")
    response = response.json()
    return jsonify({'data': response['response']['venues']})


if __name__ == "__main__":
    app.run(debug=True)
