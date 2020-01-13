from flask.views import MethodView
from app import db
from models.genre import Genre
from flask import Response
from schemas.genre_schema import GenreSchema
from flask import request
import json


class GenreAPI(MethodView):

    def get(self):
        genres = Genre.query.all()
        genres_schema = GenreSchema(many=True)
        data = genres_schema.dumps(genres)
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    def post(self):
        data = request.get_json()
        genre = Genre.from_json(json.dumps(data))
        db.session.add(genre)
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp
