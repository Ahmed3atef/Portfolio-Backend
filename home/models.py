from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="") # you didn't configure where to upload the media
    description = models.TextField(null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    facebook_url = models.URLField()
    github_url = models.URLField()
    instagram_url = models.URLField()
    linkedin_url = models.URLField()
    cv = models.FileField(upload_to="") # you didn't configure this also
    game_url = models.URLField()
    
    
    
    
