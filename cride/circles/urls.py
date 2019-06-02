""" Circles URL's """

# Django
from django.urls import include, path

# Views
from rest_framework.routers import DefaultRouter

# Views
from .views import circles as circles_views

router = DefaultRouter()
router.register(r'circles', circles_views.CircleViewSet, basename='circle')

urlpatterns = [
    path('', include(router.urls))
]
