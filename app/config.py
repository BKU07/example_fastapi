from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_password: str = ""
    database_name: str = ""
    database_username: str = ""
    secret_key: str = "default-secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"



settings = Settings() 