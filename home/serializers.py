from rest_framework import serializers
from . import models


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
    