from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.post.models import Article
from articles.post.serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer, \
    CommentCreateSerializer


class ArticleListCreateView(APIView):
    http_method_names = ["get", "post"]
    model = Article

    def get(self, request):
        queryset = Article.objects.filter(is_published=True).order_by("-created_at")
        ordering = request.query_params.get("ordering", None)
        if ordering:
            if ordering == 'up':
                queryset = queryset.order_by('-created_at')
            elif ordering == 'down':
                queryset = queryset.order_by('created_at')
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_data = PostCreateSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save(author=request.user)
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)


class ArticleDetailUpdateDeleteView(APIView):
    http_method_names = ["get", "put", "delete"]
    model = Article

    def get(self, request, pk=None):
        article = get_object_or_404(self.model, pk=pk)
        serializer = PostDetailSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        instance = get_object_or_404(self.model, pk=pk)
        serializer_data = PostCreateSerializer(instance, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        instance = get_object_or_404(self.model, pk=pk)
        instance.delete()
        return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)


class CreateComment(APIView):
    http_method_names = ["post"]

    def post(self, request, pk=None):
        request.data._mutable = True
        request.data.update({"author_id": request.user.pk, "article_id": pk})
        serializer_data = CommentCreateSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)
