from django.urls import path
from .views import generate_blog_titles

urlpatterns = [
    path("generate-titles/", generate_blog_titles, name="generate_blog_titles"),
]