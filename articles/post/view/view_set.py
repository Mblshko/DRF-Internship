from rest_framework import viewsets

from articles.post.models import Article
from articles.post.serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_published=True)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return PostDetailSerializer
        if self.action == "create":
            return PostCreateSerializer
        if self.action == "update":
            return PostCreateSerializer
        return PostListSerializer
