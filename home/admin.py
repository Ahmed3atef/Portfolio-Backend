from django.contrib import admin
from django.utils.html import format_html
from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    list_display = [
        'first_name', 
        'last_name',  
        'title', 
        ]
    readonly_fields = ['ProfileImage']
    @admin.display(description='Profile Image')
    def ProfileImage(self, instance):
        if instance.image:
            return format_html('<img src="{}" class="Image" />', instance.image.url)
        return ''
    class Media:
        css={
            'all':['admin_styles/styles.css']
        }


class SkillInline(admin.TabularInline):
    model = models.Skill

@admin.register(models.SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [SkillInline]

@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=['title', 'company','end_date']

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title', 'description', 'source_link']
    readonly_fields=['ProjectImage']
    
    @admin.display(description='Project Image')
    def ProjectImage(self, instance):
        if instance.image:
            return format_html('<img src="{}" class="Image"/>', instance.image.url)
        return ''
    
    class Media:
        css = {
            'all': ['admin_styles/styles.css']
        }


@admin.register(models.Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date_earned']
    readonly_fields = ['RewardImage']

    @admin.display(description='Reward Image')
    def RewardImage(self, instance):
        if instance.image:
            return format_html('<img src="{}" class="Image"/>', instance.image.url)
        return ''

    class Media:
        css = {
            'all': ['admin_styles/styles.css']
        }
