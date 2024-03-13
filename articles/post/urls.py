from django.urls import path, include
from rest_framework import routers

from articles.post.view.cbv import ArticleListCreateView, ArticleDetailUpdateDeleteView, CreateComment
from articles.post.view.fbv import (list_index, create, detail, update, delete, create_comment)
from articles.post.view.generic_view import ListArticleAPIView, DetailArticleAPIView, CreateArticleAPIView, \
    UpdateArticleAPIView, DeleteArticleAPIView, CreateCommentAPIView
from articles.post.view.view_set import ArticleViewSet


'''На основе  APIView'''
# urlpatterns = [
#     path("", ArticleListCreateView.as_view(), name="index"),
#     path("<uuid:uuid>/", ArticleDetailUpdateDeleteView.as_view(), name="detail"),
#     path("comment/<uuid:uuid>/", CreateComment.as_view(), name="create_comment")
# ]

'''На основе generic'''
# urlpatterns = [
#     path("", ListArticleAPIView.as_view(), name="index"),
#     path("<uuid:uuid>/", DetailArticleAPIView.as_view(), name="detail"),
#     path("create/", CreateArticleAPIView.as_view(), name="create"),
#     path("update/<uuid:uuid>/", UpdateArticleAPIView.as_view(), name="update"),
#     path("delete/<uuid:uuid>/", DeleteArticleAPIView.as_view(), name="delete"),
#     path("comment/<uuid:uuid>/", CreateCommentAPIView.as_view(), name="create_comment")
# ]

'''На основе ViewSet'''
# router = routers.DefaultRouter()
# router.register(r'', ArticleViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path("comment/<uuid:uuid>/", CreateCommentAPIView.as_view(), name="create_comment"),
# ]

'''Для каждой ручки своя функция'''
urlpatterns = [
    path("", list_index, name="index"),
    path("<uuid:uuid>/", detail, name="detail"),
    path("create/", create, name="create"),
    path("update/<uuid:uuid>/", update, name="update"),
    path("delete/<uuid:uuid>/", delete, name="delete"),
    path("comment/<uuid:uuid>/", create_comment, name="create_comment")
]
