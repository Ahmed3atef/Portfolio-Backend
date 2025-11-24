from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('profile-data', views.ProfileViewSet, basename='profile')
router.register('skills', views.SkillViewSet)


urlpatterns = [
    path('', include(router.urls))
]
