from rest_framework import serializers
from . import models
import datetime


class ProfileSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField()
    image_url = serializers.ImageField(source='image')
    cv_url = serializers.FileField(source='cv')
    
    def get_name(self, obj):
        return f"{obj.first_name()} {obj.last_name()}"
    
    
    class Meta:
        model = models.Profile
        fields = [
            'name',
            'title',
            'image_url',
            'description',
            'phone',
            'email',
            'location',
            'facebook_url',
            'github_url',
            'instagram_url',
            'linkedin_url',
            'cv_url',
            'game_url',
        ]
    

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ['name']
    
class SkillCategorySerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    
    def get_items(self,obj):
        return [skill.name for skill in obj.skill_set.all()]
    
    class Meta:
        model = models.SkillCategory
        fields = ['title', 'items']


class ExperienceSerializer(serializers.ModelSerializer):
    dates = serializers.SerializerMethodField()
    
    def get_dates(self,obj):
        return f"[{obj.start_date.strftime("%B %Y")}] - [{obj.end_date.strftime("%B %Y") if obj.end_date else 'Present'}]"
    
    class Meta:
        model = models.Experience
        fields = ['title', 'company', 'dates', 'location', 'tasks']


class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source='image')
    source_url = serializers.URLField(source='source_link')
    demo_url = serializers.URLField(source='demo_link')
    class Meta:
        model = models.Project
        fields = ['title', 'description', 'image_url', 'source_url', 'demo_url']


class RewardSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source="image")
    credential_url = serializers.URLField(source="link")
    class Meta:
        model = models.Reward
        fields = ['title', 'description', 'image_url', 'credential_url']
