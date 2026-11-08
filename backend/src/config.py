import os 

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_PASS: str
    DB_USER: str

    @property
    def BASE_DIR(self):
        base_dir = Path(__file__).parent.parent.parent
        return base_dir
    
    @property
    def BACKEND_DIR(self):
        return os.path.join(self.BASE_DIR, "backend")

    @property
    def FRONTEND_DIR(self):
        return os.path.join(self.BASE_DIR, "frontend")
    
    @property
    def STATIC_DIR(self):
        return os.path.join(self.FRONTEND_DIR, "static")
    
    @property
    def DB_URL(self):
        return ""
    

    model_config = SettingsConfigDict(env_file=".env")