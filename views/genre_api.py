from flask.views import MethodView
from app import db
from models.genre import Genre
from flask import Response
from schemas.genre_schema import GenreSchema
from flask import request, abort
from marshmallow.exceptions import ValidationError


class GenreAPI(MethodView):
    genres_schema = GenreSchema(many=True)

    def get(self):
        genres = Genre.query.all()
        data = self.genres_schema.dumps(genres)
        resp = Response(response=data, status=200, mimetype="application/json")
        return resp

    def post(self):
        data = request.get_json()
        try:
            data = self.genres_schema.load(data)
        except ValidationError as e:
            abort(400, str(e))
        db.session.add_all(data)
        db.session.commit()
        resp = Response(response=self.genres_schema.dumps(data), status=200, mimetype="application/json")
        return resp

