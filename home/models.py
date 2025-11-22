from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile/images/") # you didn't configure where to upload the media
    description = models.TextField(null=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    facebook_url = models.URLField()
    github_url = models.URLField()
    instagram_url = models.URLField()
    linkedin_url = models.URLField()
    cv = models.FileField(upload_to="cv_files/") # you didn't configure this also
    game_url = models.URLField()
    
    
    
    
