from rest_framework.views import APIView, status, Response
from users.models import User
from .serializers import AlbumSerializer
from .models import Album
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
import ipdb


class AlbumView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)
