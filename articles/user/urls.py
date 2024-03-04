from django.urls import path

from articles.user.views import register, ProfileView, ProfileUpdateView

urlpatterns = [
    path("register/", register, name="register"),
    path("profile/<slug:nickname>/", ProfileView.as_view(), name="profile"),
    path("profile/edit/<slug:nickname>/", ProfileUpdateView.as_view(), name="profile"),
]
