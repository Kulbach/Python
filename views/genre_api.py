from flask.views import MethodView
from app import db
from models.genre import Genre
from flask import Response
from schemas.genre_schema import GenreSchema
from flask import request, abort
from marshmallow.exceptions import ValidationError


class GenreAPI(MethodView):
    genres_schema = GenreSchema()

    def get(self):
        genres = Genre.query.all()
        data = self.genres_schema.dumps(genres, many=True)
        response = Response(response=data, status=200, mimetype="application/json")
        return response

    def post(self):
        data = request.get_json()
        try:
            data = self.genres_schema.load(data, many=True)
        except ValidationError as e:
            abort(400, str(e))
        db.session.add_all(data)
        db.session.commit()
        response = Response(response=self.genres_schema.dumps(data, many=True), status=200, mimetype="application/json")
        return response

    def put(self, genre_id):
        genre = Genre.query.get(genre_id)
        genre.genre = request.json.get('genre', genre.genre)
        db.session.commit()
        print(genre)
        response = Response(response=self.genres_schema.dumps(genre), status=200, mimetype="application/json")
        return response
