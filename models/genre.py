from app import db
import json

class Genre(db.Model):

    __tablename__='genres'

    genre_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50), nullable=False)

    def __init__(self, genre):
        self.genre = genre

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)

    def __repr__(self) -> str:
        return '<Genre {}>'.format(self.genre)

