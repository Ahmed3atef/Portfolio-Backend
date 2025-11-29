from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.core.mail import  BadHeaderError
from templated_mail.mail import BaseEmailMessage
from django.conf import settings
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from . import models
from . import serializers

# GET /api/profile-data/
class ProfileViewSet(ModelViewSet):
    http_method_names = ["get"]
    serializer_class = serializers.ProfileSerializer
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        obj = models.Profile.objects.select_related('user').first()
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
             
            try:

                email = BaseEmailMessage(
                    template_name='emails/contact-me.html',
                    context={
                        'name': data['name'], 
                        'email': data['email'], 
                        'message': data['message'],
                        'timestamp': timezone.now().strftime("%Y-%m-%d %H:%M")
                    }
                )
                email.send(to=[settings.EMAIL_HOST_USER], reply_to=[email])
                
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
