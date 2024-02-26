from rest_framework import generics

from articles.post.models import Article
from articles.post.serializers import PostSerializer


class ListCreateArticleAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.filter(is_published=True)
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleRUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Article.objects.filter(is_published=True)
