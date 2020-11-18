from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("save", views.save, name="save"),
    path("newPage", views.newPage, name="newPage"),
    path("random", views.random, name="random"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>",views.post, name="post")
]
