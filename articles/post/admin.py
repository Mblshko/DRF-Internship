from django.contrib import admin
from django.contrib.admin import ModelAdmin

from articles.post.models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    max_num = 3
    ordering = ('-created_at',)
    fields = ("text", "author_id")


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ["title", "created_at", "updated_at", "is_published", "author"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title", "author"]
    ordering = ["-created_at"]
    inlines = [CommentInline]

    def add_view(self, request, form_url="", extra_context=None):
        return super(ArticleAdmin, self).add_view(request)

    def change_view(self, request, object_id, form_url="", **kwargs):
        self.exclude = ("author",)
        return super(ArticleAdmin, self).change_view(request, object_id)

    @admin.action(description="Выводим текст")
    def test_message(self, request, queryset):
        self.message_user(request, message="Успешно")

    actions = [test_message]


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    pass
