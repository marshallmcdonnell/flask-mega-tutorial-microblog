import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''
    Configuration set via environment variables
    for the Flask application (or use defaults).

        SECRET_KEY: Sensitive password for forms to defend against CSRF
        DATABASE_URL: URL for the database
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
