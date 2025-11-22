from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile/images/")
    description = models.TextField(null=True)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    facebook_url = models.URLField()
    github_url = models.URLField()
    instagram_url = models.URLField()
    linkedin_url = models.URLField()
    cv = models.FileField(upload_to="cv_files/")
    game_url = models.URLField()
    

class SkillCategory(models.Model):
    title = models.CharField(max_length=255)
    
class Skill(models.Model):
    category = models.OneToOneField(SkillCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    tasks = models.JSONField(default=list)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project/images/')
    source_link = models.URLField()
    demo_link = models.URLField(null=True, blank=True)


class Reward(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='reward/images/')
    link = models.URLField()
