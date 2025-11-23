from django.db import models
from django.contrib import admin
from django.core.validators import FileExtensionValidator
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
    cv = models.FileField(upload_to="cv_files/", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    game_url = models.URLField()
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display()
    def first_name(self):
        return self.user.first_name
    @admin.display()
    def last_name(self):
        return self.user.last_name
    
        
    

class SkillCategory(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255)
    tasks = models.JSONField(default=list)
    
    class Meta:
        ordering = ['-start_date' , '-end_date']
    def __str__(self):
        return self.company

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project/images/')
    source_link = models.URLField()
    demo_link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title

class Reward(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='reward/images/')
    link = models.URLField()
    date_earned = models.DateField(null=True)
    
    class Meta:
        ordering=['-date_earned']
