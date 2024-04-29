from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import userserializer
from .models import user



# Create your views here.
'''@api_view(['GET','POST'])
def userview(request):
    if request.method=='GET':
        user=user.objects.all()
        serializer=userserializer(user,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
@api_view(['GET'])
def getuser (request,pk):
    user= user.objects.get(id=pk)
    serializer=userserializer(user,many=False)
    return Response(serializer.data)
@api_view(['PUT'])
def updateuser(request,pk):
    user=user.objects.get(id=pk)
    serializer=userserializer(instance=user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=400)
@api_view(['DELETE'])
def deleteuser(request,pk):
    user=user.objects.get(id=pk)
    user.delete()
    return Response('user deleted successfully')'''
    
class userViewSet(viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class=userserializer