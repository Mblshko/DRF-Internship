from django_filters import rest_framework as filters

from articles.post.models import Article


class ArticleFilter(filters.FilterSet):
    created_at = filters.DateFilter(field_name='created_at')

    class Meta:
        model = Article
        fields = ['title', 'created_at']
