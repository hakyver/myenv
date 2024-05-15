from .models import user
from rest_framework import viewsets, permissions
from .serializers import userserializer
class userViewSet (viewsets.ModelViewSet):
    queryset = user.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = userserializer