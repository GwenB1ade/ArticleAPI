# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: article.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'article.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rarticle.proto\x12\nArticleAPI\" \n\x0e\x44\x65tailResponse\x12\x0e\n\x06\x64\x65tail\x18\x01 \x01(\t\"B\n\x14\x43reateArticleRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\"/\n\x08UserData\x12\x11\n\tuser_uuid\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"s\n\x0f\x41rticleResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x12\r\n\x05likes\x18\x04 \x01(\x05\x12&\n\x08userdata\x18\x05 \x01(\x0b\x32\x14.ArticleAPI.UserData\"]\n\x17\x41rticleDocumentResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\x12\x17\n\x0f\x61uthor_username\x18\x04 \x01(\t\"M\n\x14\x41rticlesDocsResponse\x12\x35\n\x08\x61rticles\x18\x01 \x03(\x0b\x32#.ArticleAPI.ArticleDocumentResponse\"#\n\x0b\x41rticleUUID\x12\x14\n\x0c\x61rticle_uuid\x18\x01 \x01(\t\"\x1f\n\tUserToken\x12\x12\n\nuser_token\x18\x01 \x01(\t\"n\n\x12LikeArticleRequest\x12-\n\x0c\x61rticle_uuid\x18\x01 \x01(\x0b\x32\x17.ArticleAPI.ArticleUUID\x12)\n\nuser_token\x18\x02 \x01(\x0b\x32\x15.ArticleAPI.UserToken\"%\n\x14GetMyArticlesRequest\x12\r\n\x05token\x18\x01 \x01(\t\"A\n\x10\x41rticlesResponse\x12-\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x1b.ArticleAPI.ArticleResponse\"$\n\x14SearchArticleRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"h\n\x06\x41nswer\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x17\n\x0f\x61uthor_username\x18\x03 \x01(\t\x12\x13\n\x0b\x61uthor_uuid\x18\x04 \x01(\t\x12\x14\n\x0c\x63omment_uuid\x18\x05 \x01(\t\"d\n\x13\x43reateAnswerRequest\x12\x14\n\x0c\x63omment_uuid\x18\x01 \x01(\t\x12)\n\nuser_token\x18\x02 \x01(\x0b\x32\x15.ArticleAPI.UserToken\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\"~\n\x14\x43reateCommentRequest\x12-\n\x0c\x61rticle_uuid\x18\x01 \x01(\x0b\x32\x17.ArticleAPI.ArticleUUID\x12)\n\nuser_token\x18\x02 \x01(\x0b\x32\x15.ArticleAPI.UserToken\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\"\x96\x01\n\x0f\x43ommentResponse\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x17\n\x0f\x61uthor_username\x18\x03 \x01(\t\x12\x13\n\x0b\x61uthor_uuid\x18\x04 \x01(\t\x12\x14\n\x0c\x61rticle_uuid\x18\x05 \x01(\t\x12#\n\x07\x61nswers\x18\x06 \x03(\x0b\x32\x12.ArticleAPI.Answer\"A\n\x10\x43ommentsResponse\x12-\n\x08\x63omments\x18\x01 \x03(\x0b\x32\x1b.ArticleAPI.CommentResponse2\xc5\x05\n\x03\x41PI\x12P\n\rCreateArticle\x12 .ArticleAPI.CreateArticleRequest\x1a\x1b.ArticleAPI.ArticleResponse\"\x00\x12\x44\n\nGetArticle\x12\x17.ArticleAPI.ArticleUUID\x1a\x1b.ArticleAPI.ArticleResponse\"\x00\x12Q\n\rGetMyArticles\x12 .ArticleAPI.GetMyArticlesRequest\x1a\x1c.ArticleAPI.ArticlesResponse\"\x00\x12U\n\rSearchArticle\x12 .ArticleAPI.SearchArticleRequest\x1a .ArticleAPI.ArticlesDocsResponse\"\x00\x12K\n\x0bLikeArticle\x12\x1e.ArticleAPI.LikeArticleRequest\x1a\x1a.ArticleAPI.DetailResponse\"\x00\x12I\n\x10GetLikedArticles\x12\x15.ArticleAPI.UserToken\x1a\x1c.ArticleAPI.ArticlesResponse\"\x00\x12M\n\x0bSendComment\x12 .ArticleAPI.CreateCommentRequest\x1a\x1a.ArticleAPI.DetailResponse\"\x00\x12\x46\n\x0bGetComments\x12\x17.ArticleAPI.ArticleUUID\x1a\x1c.ArticleAPI.CommentsResponse\"\x00\x12M\n\x0c\x43reateAnswer\x12\x1f.ArticleAPI.CreateAnswerRequest\x1a\x1a.ArticleAPI.DetailResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'article_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DETAILRESPONSE']._serialized_start=29
  _globals['_DETAILRESPONSE']._serialized_end=61
  _globals['_CREATEARTICLEREQUEST']._serialized_start=63
  _globals['_CREATEARTICLEREQUEST']._serialized_end=129
  _globals['_USERDATA']._serialized_start=131
  _globals['_USERDATA']._serialized_end=178
  _globals['_ARTICLERESPONSE']._serialized_start=180
  _globals['_ARTICLERESPONSE']._serialized_end=295
  _globals['_ARTICLEDOCUMENTRESPONSE']._serialized_start=297
  _globals['_ARTICLEDOCUMENTRESPONSE']._serialized_end=390
  _globals['_ARTICLESDOCSRESPONSE']._serialized_start=392
  _globals['_ARTICLESDOCSRESPONSE']._serialized_end=469
  _globals['_ARTICLEUUID']._serialized_start=471
  _globals['_ARTICLEUUID']._serialized_end=506
  _globals['_USERTOKEN']._serialized_start=508
  _globals['_USERTOKEN']._serialized_end=539
  _globals['_LIKEARTICLEREQUEST']._serialized_start=541
  _globals['_LIKEARTICLEREQUEST']._serialized_end=651
  _globals['_GETMYARTICLESREQUEST']._serialized_start=653
  _globals['_GETMYARTICLESREQUEST']._serialized_end=690
  _globals['_ARTICLESRESPONSE']._serialized_start=692
  _globals['_ARTICLESRESPONSE']._serialized_end=757
  _globals['_SEARCHARTICLEREQUEST']._serialized_start=759
  _globals['_SEARCHARTICLEREQUEST']._serialized_end=795
  _globals['_ANSWER']._serialized_start=797
  _globals['_ANSWER']._serialized_end=901
  _globals['_CREATEANSWERREQUEST']._serialized_start=903
  _globals['_CREATEANSWERREQUEST']._serialized_end=1003
  _globals['_CREATECOMMENTREQUEST']._serialized_start=1005
  _globals['_CREATECOMMENTREQUEST']._serialized_end=1131
  _globals['_COMMENTRESPONSE']._serialized_start=1134
  _globals['_COMMENTRESPONSE']._serialized_end=1284
  _globals['_COMMENTSRESPONSE']._serialized_start=1286
  _globals['_COMMENTSRESPONSE']._serialized_end=1351
  _globals['_API']._serialized_start=1354
  _globals['_API']._serialized_end=2063
# @@protoc_insertion_point(module_scope)
