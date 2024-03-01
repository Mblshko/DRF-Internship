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
#     path("<int:pk>/", ArticleDetailUpdateDeleteView.as_view(), name="detail"),
#     path("comment/<int:pk>/", CreateComment.as_view(), name="create_comment")
# ]

'''На основе generic'''
urlpatterns = [
    path("", ListArticleAPIView.as_view(), name="index"),
    path("<int:pk>/", DetailArticleAPIView.as_view(), name="detail"),
    path("create/", CreateArticleAPIView.as_view(), name="create"),
    path("update/<int:pk>/", UpdateArticleAPIView.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteArticleAPIView.as_view(), name="delete"),
    path("comment/<int:pk>/", CreateCommentAPIView.as_view(), name="create_comment")
]

'''На основе ViewSet'''
# router = routers.DefaultRouter()
# router.register(r'', ArticleViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

'''CRUD в 2 функции'''
# urlpatterns = [
#     path("", list_and_create_index, name="index"),
#     path("<int:pk>/", update_and_delete_detail, name="detail"),
#     path("comment/<int:pk>/", create_comment, name="create_comment")
# ]

'''Для каждой ручки своя функция'''
# urlpatterns = [
#     path("", list_index, name="index"),
#     path("<int:pk>/", detail, name="detail"),
#     path("create/", create, name="create"),
#     path("update/<int:pk>/", update, name="update"),
#     path("delete/<int:pk>/", delete, name="delete"),
#     path("comment/<int:pk>/", create_comment, name="create_comment")
# ]
