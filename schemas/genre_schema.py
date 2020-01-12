from app import ma
from models.genre import Genre


class GenreSchema(ma.ModelSchema):
    class Meta:
       model = Genre
