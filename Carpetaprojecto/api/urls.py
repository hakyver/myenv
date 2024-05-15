from django.urls import path, include
from rest_framework import routers
from .api import userViewSet

router = routers.DefaultRouter()
router.register('api/users', userViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
