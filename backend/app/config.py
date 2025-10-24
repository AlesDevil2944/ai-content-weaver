from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    GOOGLE_API_KEY: str  # <--- ADD THIS LINE

    class Config:
        env_file = ".env"

settings = Settings()