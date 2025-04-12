from aioredis import from_url
from config import settings


async def get_client():
    client = from_url(settings.redis_url, db=settings.REDIS_DB)
    return client
