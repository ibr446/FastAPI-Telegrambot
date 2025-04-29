# from pydantic_settings import BaseSettings
# from functools import lru_cache
#
#
# class DatabaseSettings(BaseSettings):
#     db_host: str
#     db_port: int
#     db_user: str
#     db_pass: str
#     db_name: str
#
#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         extra = "allow"
#
#
# @lru_cache
# def get_settings():
#     return DatabaseSettings()
#
#
# class AuthConf(BaseSettings):
#     secret_key: str
#     algorithm: str
#
#     class Config:
#         env_file = ".env"
#         env_file_encoding = "utf-8"
#         extra = "allow"
#
#
# @lru_cache
# def get_auth():
#     return AuthConf()


from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")
