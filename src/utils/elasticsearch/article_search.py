from elastic_transport import ObjectApiResponse
from .base import AsyncBaseSearch
from .connect import async_client

from schemas.article_schemas import ArticleDocumentSchema, ArticleSchema


class AsyncArticleSearch(AsyncBaseSearch):
    index = 'articles'
    
    @classmethod
    async def add_article(cls, article: ArticleDocumentSchema) -> None:
        """Add an article (Create a document)

        Args:
            article (ArticleDocumentSchema): Pydantic model
        """
        
        await cls.create_document(id = article.uuid, document = article)
    
    
    @classmethod
    async def upgrade_article(cls, article: ArticleDocumentSchema) -> None:
        """Update/Edit the article (document)

        Args:
            article (ArticleDocumentSchema): Pydantic model
        """
        
        await cls.add_article(article)
    
    
    @classmethod
    async def delete_article(cls, article_uuid: str) -> None:
        """Deleting article

        Args:
            article_uuid (str): article UUID
        """
        
        await async_client.delete(
            index = cls.index,
            id = article_uuid
        )
        
    
    @classmethod
    async def get_all_articles(cls) -> dict:
        res = await async_client.search(
            index = cls.index,
        )
        
        docs = res['hits']['hits']
        return docs
        
    
    @classmethod
    async def search(cls, text: str) -> list[ArticleDocumentSchema]:
        """Search for documents by text

        Args:
            text (str): The text that is being searched for

        Returns:
            list[ArticleDocumentSchema]: Search result
        """
        uuids_docs = []
        result = []

        smatchbody = await cls.__search_match_body(text)
        smatchtitle = await cls.__search_match_title(text)
        
        sprefixtitle = await cls.__search_prefix_title(text)
        sprefixbody = await cls.__search_prefix_body(text)
        
        smatchauthor = await cls.__search_match_author(text)
        sprefixauthor = await cls.__search_prefix_author(text)
        docs = [
            smatchbody,
            smatchtitle,
            sprefixtitle,
            sprefixbody,
            smatchauthor,
            sprefixauthor
        ]
        
        for doc in docs:
            if doc:
                for i in doc:
                    if i.uuid not in uuids_docs:
                        uuids_docs.append(i.uuid)
                        result.append(i)
                    
        return result
        
    
    @classmethod
    async def __search_prefix_title(cls, prefix: str) -> list[ArticleDocumentSchema]:
        """Search for documents by prefix in the article title

        Args:
            prefix (str): Prefix

        Returns:
            list[ArticleDocumentSchema]: search result
        """
        obj = await async_client.search(
            index = cls.index,
            body = {
                'query': {
                    'prefix': {
                        'title': prefix
                    }
                }
            }
        )
        
        return cls.__convert_to_document(obj)
    
    
    @classmethod
    async def __search_prefix_body(cls, prefix: str) -> list[ArticleDocumentSchema]:
        """Search by prefix in the body of the article

        Args:
            prefix (str): Prefix

        Returns:
            list[ArticleDocumentSchema]: Search result
        """
        
        obj = await async_client.search(
            index = cls.index,
            body = {
                'query': {
                    'prefix': {
                        'body': prefix
                    }
                }
            }
        )
        
        return cls.__convert_to_document(obj)
    
    
    @classmethod
    async def __search_match_title(cls, text: str) -> list[ArticleDocumentSchema]:
        """Matching search in the article title

        Args:
            text (str): The word to be searched for

        Returns:
            list[ArticleDocumentSchema]: Search result
        """
        
        obj = await async_client.search(
            index = cls.index,
            body = {
                    'query': {
                        'match': {
                            'title': text
                        }
                    }
                }
        )
        
        return cls.__convert_to_document(obj)
    
    
    @classmethod
    async def __search_match_body(cls, text: str) -> list[ArticleDocumentSchema]:
        """Match search in the body of the article

        Args:
            text (str): The word to be searched for

        Returns:
            list[ArticleDocumentSchema]: Search result
        """
        
        obj = await async_client.search(
            index = cls.index,
            body = {
                    'query': {
                        'match': {
                            'body': text
                        }
                    }
                }
        )
        
        return cls.__convert_to_document(obj)
    

    @classmethod
    async def __search_match_author(cls, text: str) -> list[ArticleDocumentSchema]:
        """Matching search in names of authors

        Args:
            text (str): Author name

        Returns:
            list[ArticleDocumentSchema]: Search result
        """
        
        obj = await async_client.search(
            index = cls.index,
            body = {
                    'query': {
                        'match': {
                            'author_username': text
                        }
                    }
                }
        )
        
        return cls.__convert_to_document(obj)
    
    
    @classmethod
    async def __search_prefix_author(cls, text: str) -> list[ArticleDocumentSchema]:
        """Search by prefix in names of authors

        Args:
            text (str): Author name

        Returns:
            list[ArticleDocumentSchema]: Search result
        """
        
        obj = await async_client.search(
            index = cls.index,
            body = {
                    'query': {
                        'prefix': {
                            'author_username': text
                        }
                    }
                }
        )
        
        return cls.__convert_to_document(obj)
    
    
    @classmethod
    def __convert_to_document(cls, object: ObjectApiResponse) -> list[ArticleDocumentSchema]:
        """Converts the response from ElasticSearch to Pydantic schema

        Args:
            object (ObjectApiResponse): Response from ElasticSearch

        Returns:
            list[ArticleDocumentSchema]: Conversion result
        """
        
        docs = object['hits']['hits']
        list_docs = []
        for doc in docs:
            doc = doc['_source']
            list_docs.append(
                ArticleDocumentSchema(
                    uuid = doc['uuid'],
                    title = doc['title'],
                    body = doc['body'],
                    author_username = doc['author_username']
                )
            )
        
        return list_docs
    
    @classmethod
    def convert_to_document(cls, object: ObjectApiResponse) -> list[ArticleDocumentSchema]:
        """Converts the response from ElasticSearch to Pydantic schema

        Args:
            object (ObjectApiResponse): Response from ElasticSearch

        Returns:
            list[ArticleDocumentSchema]: Conversion result
        """
        
        return cls.__convert_to_document(object)
    
    