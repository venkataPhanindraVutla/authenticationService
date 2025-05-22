import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Auth Service"
    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER", "localhost")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3306")
    MYSQL_DB: str = os.getenv("MYSQL_DB")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 1440

    SQLALCHEMY_DATABASE_URI: str = ""

    def __init__(self):
        self.PROJECT_NAME = os.getenv("PROJECT_NAME", "Auth Service")
        self.MYSQL_USER = os.getenv("MYSQL_USER")
        self.MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
        self.MYSQL_SERVER = os.getenv("MYSQL_SERVER", "localhost")
        self.MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
        self.MYSQL_DB = os.getenv("MYSQL_DB")
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.ALGORITHM = os.getenv("ALGORITHM", "HS256")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
        self.REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", 1440))

        if self.MYSQL_USER is None or self.MYSQL_PASSWORD is None or self.MYSQL_DB is None:
            raise ValueError("MYSQL_USER, MYSQL_PASSWORD, and MYSQL_DB must be set in the environment.")
        if self.SECRET_KEY is None:
            raise ValueError("SECRET_KEY must be set in the environment.")

        self.SQLALCHEMY_DATABASE_URI = self.assemble_db_connection()

    def assemble_db_connection(self) -> str:
        return f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

settings = Settings()