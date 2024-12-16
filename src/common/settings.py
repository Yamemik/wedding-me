from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "wedding-me"
    debug: bool = True


settings = Settings()
