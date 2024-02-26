from django.urls import path, include
from rest_framework import routers

from articles.post.view.cbv import ArticleListCreateView, ArticleDetailUpdateDeleteView
from articles.post.view.fbv import (list_and_create_index, update_and_delete_detail,
                                    list_index, create, detail, update, delete)
from articles.post.view.generic_view import ListCreateArticleAPIView, ArticleRUD
from articles.post.view.view_set import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'', ArticleViewSet)

# TODO: Маршруты для представлений на основе классов
'''На основе  APIView'''
# urlpatterns = [
#     path("", ArticleListCreateView.as_view(), name="index"),
#     path("<int:pk>/", ArticleDetailUpdateDeleteView.as_view(), name="detail"),
# ]

'''На основе generic'''
# urlpatterns = [
#     path("", ListCreateArticleAPIView.as_view(), name="index"),
#     path("<int:pk>/", ArticleRUD.as_view(), name="detail"),
# ]

'''На основе ViewSet'''
urlpatterns = [
    path('', include(router.urls)),
]

# TODO: Маршруты для представлений на основе функций
'''CRUD в 2 функции'''
# urlpatterns = [
#     path("", list_and_create_index, name="index"),
#     path("<int:pk>/", update_and_delete_detail, name="detail"),
# ]

'''Для каждой ручки своя функция'''
# urlpatterns = [
#     path("", list_index, name="index"),
#     path("<int:pk>/", detail, name="detail"),
#     path("create/", create, name="create"),
#     path("update/<int:pk>/", update, name="update"),
#     path("delete/<int:pk>/", delete, name="delete")
# ]
