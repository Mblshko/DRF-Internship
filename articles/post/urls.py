from django.contrib import admin
from django.urls import path
from articles.post.view.fbv import (list_and_create_index, update_and_delete_detail,
                                    list_index, create, detail, update, delete)
from articles.post.view.generic_view import ListCreateArticleAPIView

urlpatterns = [
    path("", list_and_create_index, name="index"),
    path("<int:pk>", update_and_delete_detail, name="detail"),
]

# urlpatterns = [
#     path("", list_index, name="index"),
#     path("<int:pk>", detail, name="detail"),
#     path("create/", create, name="create"),
#     path("update/<int:pk>", update, name="update"),
#     path("delete/<int:pk>", delete, name="delete")
# ]

# urlpatterns = [
#     path("", ListCreateArticleAPIView.as_view(), name="index"),
#     path("<int:pk>", detail, name="detail"),
# ]
