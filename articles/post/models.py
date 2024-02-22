from django.db import models
from articles.user.models import User


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название статьи")
    content = models.TextField(max_length=10000, verbose_name="Текст статьи")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать?")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    text = models.TextField(max_length=1000, unique=True, verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор",
                                  related_name="comment")
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статьи",
                                   related_name="comment")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
