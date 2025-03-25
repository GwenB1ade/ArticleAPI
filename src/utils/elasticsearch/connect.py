from elasticsearch import AsyncElasticsearch
from config import settings

async_client = AsyncElasticsearch(
    [
        {
        'host': settings.ELASTIC_HOST,
        'port': settings.ELASTIC_PORT,
        'scheme': "http"  
        }
    ],
    http_auth = ('elastic', settings.ELASTIC_PASSWORD)
)