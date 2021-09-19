import os
from typing import List, Type
from pydantic import BaseSettings
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
env_path = os.path.join(basedir, '.env')

class Settings(BaseSettings):
    CONFIG_NAME: str = "base"
    USE_MOCK_EQUIVALENCY: bool = False
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    print(env_path)
    class Config:
        load_dotenv(env_path)
        # env_file = env_path
        env_file_encoding = 'utf-8'


class DevelopmentConfig(Settings):
    CONFIG_NAME: str = "dev"
    SECRET_KEY: str = os.getenv(
        "DEV_SECRET_KEY", "something"
    )
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL: str = os.getenv('DB_DEV_URI')


class TestingConfig(Settings):
    CONFIG_NAME: str = "test"
    SECRET_KEY: str = os.getenv("TEST_SECRET_KEY", "something")
    DEBUG: bool = True
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URL: str = os.getenv('DB_URI')


class ProductionConfig(Settings):
    CONFIG_NAME: str = "prod"
    SECRET_KEY: str = os.getenv("PROD_SECRET_KEY", "something")
    DEBUG: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL: str = os.getenv('DB_URI')


def get_config(config):
    print(config_by_name[config])
    return config_by_name[config]


EXPORT_CONFIGS: List[Type[Settings]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]
config_by_name = {cfg().CONFIG_NAME: cfg() for cfg in EXPORT_CONFIGS}