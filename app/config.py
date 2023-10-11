
production = False

if production:
    # --------------- Production Config ---------------
    class Config(object):
        DEBUG = False
        DEVELOPMENT = False
        SECRET_KEY = "afijoi23jooHOIFOEIKJLDFJLSDJFaoefhaognowe2342523413joijfao2342"
        SQLALCHEMY_DATABASE_URI = "sqlite:///wleness.db"
        SQLALCHEMY_TRACK_MODIFICATIONS = False

else:
    # --------------- Development Config ---------------
    class Config(object):
        DEBUG = True
        DEVELOPMENT = True
        SECRET_KEY = "afijoi23jooHOIFOEIKJLDFJLSDJFaoefhaognowe2342523413joijfao2342"
        SQLALCHEMY_DATABASE_URI = "sqlite:///wleness.db"
        SQLALCHEMY_TRACK_MODIFICATIONS = False