from flask.views import MethodView
from models.genre import Genre
from flask import Response
from schemas.genre_schema import GenreSchema


class GenreAPI(MethodView):

    def get(self):
        genres = Genre.query.all()
        genres_schema = GenreSchema(many=True)
        data = genres_schema.dumps(genres)
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp
