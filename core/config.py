from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SERVER_HOST: AnyHttpUrl = "http://localhost"
    
    class config:
        case_sensitive = True
        
settings = Settings()