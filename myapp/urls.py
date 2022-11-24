from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("content", views.content, name="content"),
    path("register", views.register, name="register"),
    path("404", views.page, name="page"),
]
