from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env.local', extra='ignore', case_sensitive=False
    )

    # PostgreSQL database settings
    db_host: str = 'localhost'
    db_port: int = 5432
    db_name: str = 'books_db'
    db_user: str = 'postgres'
    db_password: str = None  # Password can be optional

    # Other settings (optional)
    debug: bool = False

    @property
    def database_url(self) -> str:
        """Construct the async database URL."""
        if self.db_password:
            return (
                f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}:'
                f'{self.db_port}/{self.db_name}'
            )
        else:
            return (
                f'postgresql://{self.db_user}@{self.db_host}:{self.db_port}/{self.db_name}'
            )

    @property
    def async_database_url(self) -> str:
        """Construct the async database URL for asyncpg."""
        return self.database_url.replace("postgresql://", "postgresql+asyncpg://")


settings = Settings()

if __name__ == '__main__':
    print(settings.model_dump())
    print(settings.database_url)
    print(settings.async_database_url)
