from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.urls import reverse
from articles.user.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse("profile", kwargs={"nickname": self.nickname})

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
