from app import create_app
from models import Genre, GenreSchema
from flask import Response

app = create_app()


def main():
    app.run()


@app.route('/api/genres', methods=['GET'])
def get_genres():
    genres = Genre.query.all()
    genres_schema = GenreSchema(many=True)
    data = genres_schema.dumps(genres)
    resp = Response(response=data, status=200, mimetype="application/json")
    return resp


if __name__ == '__main__':
    main()

