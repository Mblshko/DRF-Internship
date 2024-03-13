from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError, OperationalError

from articles.post.models import Article
from articles.post.serializers import (PostCreateSerializer, PostListSerializer,
                                       PostDetailSerializer, CommentCreateSerializer)


@api_view()
def list_index(request):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    ordering = request.query_params.get("ordering", None)
    if ordering:
        if ordering == "DESC":
            queryset = queryset.order_by("-created_at")
        elif ordering == "ASC":
            queryset = queryset.order_by("created_at")
    serializer_data = PostListSerializer(queryset, many=True)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create(request):
    serializer_class = PostCreateSerializer(data=request.data)
    if serializer_class.is_valid():
        try:
            serializer_class.save(author=request.user)
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        except ValueError:
            return Response({"message": "Пользователь не авторизован"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def detail(request, uuid):
    instance = get_object_or_404(Article, id=uuid)
    serializer_data = PostDetailSerializer(instance)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update(request, uuid):
    instance = get_object_or_404(Article, id=uuid)
    serializer_class = PostCreateSerializer(instance, data=request.data, partial=True)
    if serializer_class.is_valid():
        try:
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
        except ValueError:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete(request, uuid):
    instance = get_object_or_404(Article, id=uuid)
    try:
        instance.delete()
        return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)
    except IntegrityError as error:
        return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)
    except OperationalError as error_o:
        return Response({"message": error_o}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_comment(request, uuid):
    request.data._mutable = True
    request.data.update({"author_id": request.user.pk, "article_id": uuid})
    serializer_class = CommentCreateSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
