from flask import current_app as app

from views.genre_api import GenreAPI

genre_view = GenreAPI.as_view('genres_api')
app.add_url_rule('/api/genres', view_func=genre_view, methods=['GET'])
app.add_url_rule('/api/genres', view_func=genre_view, methods=['POST'])