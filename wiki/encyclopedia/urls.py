from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("save", views.save, name="save"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>",views.post, name="post")
]
