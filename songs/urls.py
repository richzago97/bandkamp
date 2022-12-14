from django.urls import path

from . import views
from songs import views as song_views

urlpatterns = [
    path("songs/", views.SongView.as_view()),
    path("songs/<int:album_id>", song_views.SongView.as_view()),
]
