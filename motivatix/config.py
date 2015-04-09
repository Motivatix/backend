class DevelopmentConfig():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///motivatix.db'
    DEBUG = True


class TestingConfig():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
