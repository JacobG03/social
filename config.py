import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # General
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-secret-key'
    
    # Database config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_IRL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    
    # Mail config
    MAIL_SERVER='smtp.gmail.com'
    MAIL_USERNAME=''
    MAIL_PASSWORD=''
    MAIL_PORT=465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
