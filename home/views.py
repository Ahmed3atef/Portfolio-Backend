from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.core.mail import EmailMessage, BadHeaderError
from django.conf import settings
from rest_framework.viewsets import ModelViewSet, GenericViewSet

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

# GET /api/skills
class SkillViewSet(ModelViewSet):
    http_method_names = ['get']
    permission_classes=[AllowAny]
    queryset = models.SkillCategory.objects.prefetch_related('skill_set').all()
    serializer_class = serializers.SkillCategorySerializer

# GET /api/experience
class ExperienceViewSet(ModelViewSet):
    http_method_names = ['get']
    permission_classes = [AllowAny]
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer

# GET /api/projects
class ProjectViewSet(ModelViewSet):
    http_method_names = ['get']
    permission_classes = [AllowAny]
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

# GET / api/rewards
class RewardViewSet(ModelViewSet):
    http_method_names = ['get']
    permission_classes = [AllowAny]
    queryset = models.Reward.objects.all()
    serializer_class = serializers.RewardSerializer

# POST /api/contact
class ContactViewSet(GenericViewSet):
    http_method_names = ['post']
    permission_classes = [AllowAny]
    serializer_class = serializers.ContactSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = serializers.ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.validated_data
            
            email_body = (
                f"Name: {data.get('name')}\n"
                f"Email: {data.get('email')}\n\n"
                f"Message:\n{data.get('message')}"
            )
            
            try:

                email = EmailMessage(
                    subject=f"New contact from {data.get('name')}",
                    body=email_body,
                    from_email=settings.EMAIL_HOST_USER,
                    to=[settings.EMAIL_HOST_USER],
                    reply_to=[data.get('email')]
                )
                email.send(fail_silently=False)
                return Response({'message': 'ok'}, status=status.HTTP_200_OK)
            except BadHeaderError:
                return Response(
                    {'error': 'Invalid header found.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Exception as e:
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
