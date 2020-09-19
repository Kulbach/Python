from app import ma
from models import Genre


class GenreSchema(ma.ModelSchema):
    class Meta:
       model = Genre
    movies = ma.Nested('MovieSchema', many=True)
