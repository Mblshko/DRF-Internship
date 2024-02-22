from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from articles.post.models import Article
from articles.post.serializers import PostSerializer


@api_view(["GET", "POST"])
def list_and_create_index(request):
    if request.method == "POST":
        serializer_class = PostSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save(author=request.user)
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_data = PostSerializer(queryset, many=True)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view(["GET", "PUT", "DELETE"])
def update_and_delete_detail(request, pk):
    instance = get_object_or_404(Article, pk=pk)
    if request.method == "PUT":
        serializer_class = PostSerializer(instance, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
    if request.method == "DELETE":
        instance.delete()
        return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)
    serializer_data = PostSerializer(instance)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view()
def list_index(request):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_data = PostSerializer(queryset, many=True)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create(request):
    serializer_class = PostSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save(author=request.user)
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view()
def detail(request, pk):
    instance = get_object_or_404(Article, pk=pk)
    serializer_data = PostSerializer(instance)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update(request, pk):
    instance = get_object_or_404(Article, pk=pk)
    serializer_class = PostSerializer(instance, data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
        return Response(serializer_class.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete(request, pk):
    instance = get_object_or_404(Article, pk=pk)
    instance.delete()
    return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)
