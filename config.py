import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_DEV_URL')


class Development(Config):
    DEBUG = True


app_config = {
    'development': Development
}