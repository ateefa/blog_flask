import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    db_path = os.path.join(os.path.dirname(__file__), 'site.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "nmm@gmail.com"
    MAIL_PASSWORD = "qwertyuiop"