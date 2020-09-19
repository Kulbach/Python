from app import ma
from models import Movie


class MovieSchema(ma.ModelSchema):
    class Meta:
       model = Movie