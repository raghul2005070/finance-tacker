class Config:
    SECRET_KEY = "personal_finance_secret"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@localhost/finance_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False