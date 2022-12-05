from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="home"),
    path("index",views.index),
    path("planets", views.planets, name="planets"),
    path("category/<slug:slug>", views.planet_category,name="planet_category"),
    path("galaxies", views.galaxies, name = "galaxies"),
    path("blog-details/<slug:slug>", views.blog_details ,name = "blog_details")
]