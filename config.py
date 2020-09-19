import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_DEV_URL')


class Development(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TESTING = True


app_config = {
    'development': Development
}
