class Config:
    SQLALCHEMY_DATABASE_URI = "mysql://root:12345@localhost:3306/test"
    MYSQL_ROOT_USER = "root"
    MYSQL_ROOT_PASSWORD = "12345"
    SQLALCHEMY_TRACK_MODIFICATIONS = False