from app import db


class Movie(db.Model):

    __tablename__='movies'

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    movie_cost = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), nullable=False)

    def __repr__(self) -> str:
        return '<Movie {}>'.format(self.title)