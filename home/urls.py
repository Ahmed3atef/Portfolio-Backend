from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('profile-data', views.ProfileViewSet, basename='profile')
router.register('skills', views.SkillViewSet)
router.register('experience', views.ExperienceViewSet)
router.register('projects', views.ProjectViewSet)
router.register('rewards', views.RewardViewSet)
router.register('contact', views.ContactViewSet, basename='contact')


urlpatterns = [
    path('', include(router.urls))
]
