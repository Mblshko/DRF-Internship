from rest_framework import serializers

from articles.post.models import Article


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["id", "title", "content", "is_published"]
