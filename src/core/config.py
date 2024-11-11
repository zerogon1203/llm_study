from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API 설정
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Project"
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = True
    
    # CORS 설정
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    
    # 환경 설정
    ENVIRONMENT: Optional[str] = "dev"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 