from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('profile-data', views.ProfileViewSet, basename='profile')


urlpatterns = [
    path('', include(router.urls))
]
