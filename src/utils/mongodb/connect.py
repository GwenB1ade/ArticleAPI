from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection

from config import settings

# client = AsyncIOMotorClient(
#     settings.mongo_url,
# )

client = AsyncMongoClient(settings.mongo_url)

db = client["ArtcileDB"]
comments_colleclion: AsyncCollection = db["comments"]


async def ping():
    try:
        await client.admin.command("ping")
        print("Success")
    except Exception as e:
        print(f"Fail: {e}")
