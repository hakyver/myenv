from django.urls import path, include
from rest_framework import routers,viewsets
from .api import userViewSet

router = routers.DefaultRouter()
router.register('api/users',userViewSet,'api')


urlpatterns = router.urls