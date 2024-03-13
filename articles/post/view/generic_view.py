from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError, OperationalError
from rest_framework import generics, status
from rest_framework.response import Response

from articles.post.models import Article
from articles.post.serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer, \
    CommentCreateSerializer


class ListArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostListSerializer

    def get(self, request, *args, **kwargs):
        queryset = Article.objects.filter(is_published=True).order_by("-created_at")
        ordering = request.query_params.get("ordering", None)
        if ordering:
            if ordering == "DESC":
                queryset = queryset.order_by("-created_at")
            elif ordering == "ASC":
                queryset = queryset.order_by("created_at")
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailArticleAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostDetailSerializer

    def get_object(self):
        return Article.objects.get(id=self.kwargs.get("uuid"))


class CreateArticleAPIView(generics.CreateAPIView):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpdateArticleAPIView(generics.UpdateAPIView):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostCreateSerializer

    # TODO: Задать partial
    def get_object(self):
        return Article.objects.get(id=self.kwargs.get("uuid"))


class DeleteArticleAPIView(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        instance = get_object_or_404(Article, id=kwargs["uuid"])
        try:
            instance.delete()
            return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)
        except IntegrityError as error:
            return Response({"message": error}, status=status.HTTP_400_BAD_REQUEST)
        except OperationalError as error_o:
            return Response({"message": error_o}, status=status.HTTP_400_BAD_REQUEST)


class CreateCommentAPIView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data.update({"author_id": request.user.pk, "article_id": kwargs["uuid"]})
        serializer_class = CommentCreateSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
