import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "MPLAYER API"
    #TODO: DATABASE_URL: str = "TODO"

    class Config:
        env_file = ".env"

settings = Settings()
