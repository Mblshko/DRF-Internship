import uuid

from django.db import models
from articles.user.models import User


class TimestampModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    class Meta:
        abstract = True


class Article(TimestampModel):
    title = models.CharField(max_length=255, verbose_name="Название статьи")
    content = models.TextField(max_length=10000, verbose_name="Текст статьи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовать?")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(TimestampModel):
    text = models.TextField(max_length=1000, unique=True, verbose_name="Текст комментария")
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор",
                                  related_name="comment")
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статьи",
                                   related_name="comment")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
