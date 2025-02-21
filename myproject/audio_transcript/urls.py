from django.urls import path
from .views import transcribe_audio

urlpatterns = [
    path("generate-transcript/", transcribe_audio, name="transcribe_audio"),
]