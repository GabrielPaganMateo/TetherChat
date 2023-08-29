from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="LogIn"),
    path("index/", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("chat/", views.chat, name="chat"),
]