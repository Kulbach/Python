from views.genre_api import GenreAPI


def init_routes(app):
    genre_view = GenreAPI.as_view('genres_api')
    app.add_url_rule('/api/genres', view_func=genre_view, methods=['GET'])
    app.add_url_rule('/api/genres', view_func=genre_view, methods=['POST'])
    app.add_url_rule('/api/genres/<int:genre_id>', view_func=genre_view, methods=['PUT'])