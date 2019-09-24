from models.user import User
import db
from flask import Flask, request, json, make_response
from scraper import *  # Web Scraping utility functions for Online Clubs with Penn.

app = Flask(__name__)


@app.route('/')
def main():
    return "Welcome to Penn Club Review!"


@app.route('/api')
def api():
    return "Welcome to the Penn Club Review API!."


@app.route('/api/clubs', methods=["GET"])
def read_clubs():
    clubs = db.get_clubs()
    if clubs is not None:
        return json.jsonify(clubs)
    else:
        return "No clubs found", 400


@app.route('/api/clubs', methods=["POST"])
def create_one_club():
    msg = db.create_one_club(request.form)
    if msg == "success":
        return msg, 201
    else:
        return msg, 400


@app.route('/api/clubs/similar', methods=["POST"])
def create_one_club():
    if "club_name" in request.form:
        n = request.form["n"] if "n" in request.form else 3
        msg = db.get_similar_club(request.form["club_name"], n)
        if type(msg) == str:
            return msg, 400
        else:
            return json.jsonify(msg)
    return "club_name is required to favorite", 400


@app.route('/api/user/<username>', methods=["GET"])
def read_one_user(username):
    user_data = db.get_user(username)
    if type(user_data) == str:
        return user_data, 400
    else:
        return json.jsonify(user_data)


@app.route("/api/favorite", methods=["POST"])
def favorite():
    if "username" in request.form:
        if "club_name" in request.form:
            msg = db.favorite(request.form["username"], request.form["club_name"])
            if msg == "success":
                return msg, 200
            else:
                return msg, 400
        return "club_name is required to favorite", 400
    if "club_name" in request.form:
        return "username is required to favorite", 400

    return "username and club_name are required to favorite", 400


@app.route("/api/favorite", methods=["POST"])
def favorite():
    if "username" in request.form:
        if "club_name" in request.form:
            msg = db.favorite(request.form["username"], request.form["club_name"])
            if msg == "success":
                return msg, 200
            else:
                return msg, 400
        return "club_name is required to favorite", 400
    if "club_name" in request.form:
        return "username is required to favorite", 400

    return "username and club_name are required to favorite", 400


@app.route("/api/favorite", methods=["POST"])
def favorite():
    if "username" in request.form:
        if "club_name" in request.form:
            msg = db.unfavorite(request.form["username"], request.form["club_name"])
            if msg == "success":
                return msg, 200
            else:
                return msg, 400
        return "club_name is required to favorite", 400

    if "club_name" in request.form:
        return "username is required to favorite", 400

    return "username and club_name are required to favorite", 400


if __name__ == '__main__':
    db.populate()
    app.run(port=3000)
