from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework import generics
from django.shortcuts import get_object_or_404
import ipdb


class SongView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    lookup_url_kwarg = "album_id"

    def get_queryset(self):
        album_id = self.kwargs[self.lookup_url_kwarg]
        return Song.objects.filter(id=album_id)

    def perform_create(self, serializer):
        album = get_object_or_404(Album, id=self.kwargs[self.lookup_url_kwarg])
        serializer.save(album=album)
