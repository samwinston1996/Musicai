from django.urls import path
from .views import showcase


urlpatterns = [
    path("showcase/", showcase, name="showcase")
]