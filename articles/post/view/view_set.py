from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError, OperationalError
from rest_framework import viewsets, status
from rest_framework.response import Response

from articles.post.models import Article
from articles.post.serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(is_published=True)
    lookup_field = "uuid"

    def list(self, request, *args, **kwargs):
        queryset = Article.objects.filter(is_published=True).order_by("-created_at")
        ordering = request.query_params.get("ordering", None)
        if ordering:
            if ordering == "DESC":
                queryset = queryset.order_by("-created_at")
            elif ordering == "ASC":
                queryset = queryset.order_by("created_at")
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    def get_object(self):
        return Article.objects.get(id=self.kwargs.get("uuid"))

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(Article, id=kwargs["uuid"])
        try:
            instance.delete()
            return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)
        except IntegrityError as error:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)
        except OperationalError as error_o:
            return Response({"message": error_o}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
