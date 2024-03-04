from rest_framework import generics, status
from rest_framework.response import Response

from articles.post.models import Article
from articles.post.serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer, \
    CommentCreateSerializer


class ListArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostListSerializer


class DetailArticleAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostDetailSerializer


class CreateArticleAPIView(generics.CreateAPIView):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UpdateArticleAPIView(generics.UpdateAPIView):
    queryset = Article.objects.filter(is_published=True).order_by("-created_at")
    serializer_class = PostCreateSerializer


class DeleteArticleAPIView(generics.DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        instance = Article.objects.get(pk=kwargs['pk'])
        instance.delete()
        return Response({"message": "Успешно удалено"}, status=status.HTTP_200_OK)


class CreateCommentAPIView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data.update({"author_id": request.user.pk, "article_id": kwargs['pk']})
        serializer_class = CommentCreateSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
