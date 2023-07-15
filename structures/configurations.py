import logging

from dataclasses import dataclass

from os import getenv

from sqlalchemy.engine import URL


@dataclass
class DatabaseConfig:
    """Database connection variables"""
    name: str = "BOT"
    user: str = "BOT"
    passwd: str = "123321"
    port: int = 5432
    host: str = "localhost"

    driver: str = "asyncpg"
    database_system: str = "postgresql"

    def build_connection_str(self) -> str:
        """
        This function build a connection string
        """
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)




@dataclass
class BotConfig:
    """Bot configuration"""
    token: str = ""


@dataclass
class APIConfig:
    """Bot configuration"""
    open_ai_key: str = getenv("OPENAI_KEY", "")


@dataclass
class Configuration:
    """All in one configuration's class"""

    debug = bool(getenv("DEBUG"))
    logging_level = int(getenv("LOGGING_LEVEL", logging.INFO))

    db = DatabaseConfig()
    redis = RedisConfig()
    bot = BotConfig()
    api = APIConfig()


conf = Configuration()