from rest_framework import serializers
from .models import user

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields='__all__' #los datos que pueden ser consultados
        read_only_fields= ('fecha',) #para que la fecha no pueda ser editada
