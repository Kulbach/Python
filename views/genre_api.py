from flask.views import MethodView
from app import db
from models import Genre
from flask import Response
from schemas.genre_schema import GenreSchema
from flask import request, abort
from marshmallow.exceptions import ValidationError
import json


class GenreAPI(MethodView):
    genres_schema = GenreSchema()

    def get(self, genre_id):
        if genre_id is None:
            genres = Genre.query.all()
            data = self.genres_schema.dumps(genres, many=True)
            response = Response(response=data, status=200, mimetype="application/json")
        else:
            genre = Genre.query.get(genre_id)
            if not genre:
                abort(Response(response='{"message": "Requested genre not found"}', status=404,
                               mimetype="application/json"))
            response = Response(response=self.genres_schema.dumps(genre), status=200, mimetype="application/json")
        return response

    def post(self):
        data = request.get_json()
        try:
            data = self.genres_schema.load(data, many=True)
        except ValidationError as e:
            abort(Response(response=json.dumps(e.messages), status=400,
                           mimetype="application/json"))
        db.session.add_all(data)
        db.session.commit()
        response = Response(response=self.genres_schema.dumps(data, many=True), status=200, mimetype="application/json")
        return response

    def put(self, genre_id):
        genre = Genre.query.get(genre_id)
        if not genre:
            abort(Response(response='{"message": "Requested genre not found"}', status=404,
                           mimetype="application/json"))
        genre.genre = request.json.get('genre', genre.genre)
        db.session.commit()
        response = Response(response=self.genres_schema.dumps(genre), status=200, mimetype="application/json")
        return response

    def delete(self, genre_id):
        genre = Genre.query.get(genre_id)
        if not genre:
            abort(Response(response='{"message": "Requested genre not found"}', status=404,
                           mimetype="application/json"))
        db.session.delete(genre)
        db.session.commit()
        response = Response(response=self.genres_schema.dumps(genre), status=200, mimetype="application/json")
        return response
