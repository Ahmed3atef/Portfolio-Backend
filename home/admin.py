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
    def ProfileImage(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="ProfileImage" />')
        return ''
    class Media:
        css={
            'all':['admin_styles/styles.css']
        }
