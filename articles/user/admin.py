from django.contrib import admin

from articles.user.models import User, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {"nickname": ("nickname", )}


admin.site.register(User)
