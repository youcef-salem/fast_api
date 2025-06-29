from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(
BaseSettings

):
    Database_url:str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
