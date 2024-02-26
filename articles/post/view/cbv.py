from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from articles.post.models import Article
from articles.post.serializers import PostSerializer


class ArticleListCreateView(APIView):
    http_method_names = ["get", "post"]
    model = Article
    serializer_class = PostSerializer

    def get(self, request):
        queryset = Article.objects.filter(is_published=True)
        ordering = request.query_params.get("ordering", None)
        if ordering:
            if ordering == 'up':
                queryset = queryset.order_by('-created_at')
            elif ordering == 'down':
                queryset = queryset.order_by('created_at')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save(author=request.user)
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)


class ArticleDetailUpdateDeleteView(APIView):
    http_method_names = ["get", "put", "delete"]
    model = Article
    serializer_class = PostSerializer

    def get(self, request, pk=None):
        article = get_object_or_404(self.model, pk=pk)
        serializer = self.serializer_class(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        instance = get_object_or_404(self.model, pk=pk)
        serializer_data = self.serializer_class(instance, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        instance = get_object_or_404(self.model, pk=pk)
        instance.delete()
        return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)
