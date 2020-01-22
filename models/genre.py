from app import db


class Genre(db.Model):

    __tablename__='genres'

    genre_id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50), nullable=False)
    movies = db.relationship('Movie', backref='genre', lazy='dynamic')

    def __repr__(self) -> str:
        return '<Genre {}>'.format(self.genre)

