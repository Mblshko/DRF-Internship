from rest_framework import serializers

from articles.post.models import Article, Comment


class CommentViewSerializer(serializers.ModelSerializer):
    author_id = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Comment
        fields = ["text", "author_id"]


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["text", "author_id", "article_id"]


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "content", "author"]


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=False, read_only=True)
    comment = CommentViewSerializer(many=True)

    class Meta:
        model = Article
        fields = ["id", "title", "content", "is_published", "author", "comment"]


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["title", "content", "is_published"]


class PostSerializer(serializers.ModelSerializer):
    pass
