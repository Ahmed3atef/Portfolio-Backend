from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from . import models
from . import serializers

# GET /api/profile-data/
class ProfileViewSet(ModelViewSet):
    http_method_names = ["get"]
    queryset = models.Profile.objects.select_related('user').all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        obj = self.get_queryset().first()
        if obj is None:
            return Response({"detail": "No profiles found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

