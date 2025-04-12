from .connect import async_client
from pydantic import BaseModel


class AsyncBaseSearch:
    index: str

    @classmethod
    async def create_index(cls):
        await async_client.indices.create(index=cls.index)

    @classmethod
    async def create_document(cls, id: int | str, document: BaseModel) -> None:
        """A function for creating a document in ElasticSearch

        Args:
            id (int | str): Document ID
            document (BaseModel): A document of the BaseModel Pydantic type.
        """

        await async_client.index(index=cls.index, id=id, document=document.model_dump())

    @classmethod
    async def get_document(cls, id: int | str) -> dict:
        """Get a document by ID

        Args:
            id (int | str): Document ID

        Returns:
            dict: Document data
        """

        doc = await async_client.get(index=cls.index, id=id)

        return doc
