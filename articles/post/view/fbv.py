from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from articles.post.models import Article
from articles.post.serializers import (PostCreateSerializer, PostListSerializer,
                                       PostDetailSerializer, CommentCreateSerializer)


@api_view()
def list_index(request):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_data = PostListSerializer(queryset, many=True)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create(request):
    serializer_class = PostCreateSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save(author=request.user)
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def detail(request, pk):
    instance = get_object_or_404(Article, pk=pk)
    serializer_data = PostDetailSerializer(instance)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update(request, pk):
    instance = get_object_or_404(Article, pk=pk)
    serializer_class = PostCreateSerializer(instance, data=request.data, partial=True)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete(request, pk):
    instance = get_object_or_404(Article, pk=pk)
    instance.delete()
    return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_comment(request, pk):
    request.data._mutable = True
    request.data.update({"author_id": request.user.pk, "article_id": pk})
    serializer_class = CommentCreateSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
