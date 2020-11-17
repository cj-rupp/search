from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("wiki/save", views.save, name="save"),
    path("wiki/newPage", views.newPage, name="newPage"),
    path("wiki/random", views.random, name="random"),
    path("wiki/edit/<str:title>", views.edit, name="edit"),
    path("wiki/<str:title>",views.post, name="post")
]
