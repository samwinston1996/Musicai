from django.urls import path
from .views import home, generator, save_to_gallery


urlpatterns = [
    path("", home, name="home"),
    path("generator/", generator, name="generator"),
    path("save_to_gallery/", save_to_gallery, name="save_to_gallery")
]