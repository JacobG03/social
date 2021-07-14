import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_IRL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    
    MAIL_SERVER='smtp.gmail.com'
    MAIL_USERNAME='jaqobek1995@gmail.com'
    MAIL_PASSWORD='bznkefoonpsgmfen'
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False