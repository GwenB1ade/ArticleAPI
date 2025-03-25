from pydantic_settings import BaseSettings, EnvSettingsSource, SettingsConfigDict


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_PORT: int
    DB_HOST: str

    JWT_SECRET: str
    SESSION_SECRET: str
    JWT_ALGORITHM: str
    
    MONGO_PASS: str
    MONGO_USER: str
    MONGO_HOST: str
    MONGO_PORT: int
    
    REDIS_PORT: int
    REDIS_HOST: str
    REDIS_DB: int
    
    BROKER_PORT: int
    BROKER_HOST: str
    BROKER_USER: str
    BROKER_PASS: str
    BROKER_ROUTING_NAME: str
    
    ELASTIC_HOST: str
    ELASTIC_PORT: int
    ELASTIC_PASSWORD: str
    ELASTIC_USERNAME: str
    ELASTIC_API_KEY: str
    ELASTIC_ENCODED: str
    
    
    @property
    def database_url(self):
        return f'postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    
    @property
    def async_database_url(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
    
    
    @property
    def redis_url(self):
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}'
    
    
    @property
    def jwt_secret(self):
        return self.JWT_SECRET
    
    
    @property
    def mongo_url(self):
        return f'mongodb://{self.MONGO_USER}:{self.MONGO_PASS}@localhost:27017/?authSource=admin'
    
    
    @property
    def origins(self):
        return [
            "http://localhost:8000",
        ]
    
    model_config = SettingsConfigDict(env_file = '../.env')
    

settings = Settings()