from flask import current_app as app

from views.genre_api import GenreAPI

app.add_url_rule('/api/genres', view_func=GenreAPI.as_view('genres_api'))