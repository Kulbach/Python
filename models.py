from app import db, ma


class Genre(db.Model):

    __tablename__='genres'

    genre_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return '<Genre {}>'.format(self.genre)


class GenreSchema(ma.ModelSchema):
    class Meta:
       model = Genre
