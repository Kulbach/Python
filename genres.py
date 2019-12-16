from app import db
from models import Genre, GenreSchema


def read_all():
    genres = Genre.query.all()
    genres_schema = GenreSchema(many=True)
    data = genres_schema.dump(genres).data
    return data