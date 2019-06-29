from rest_framework import viewsets,status
from rest_framework.views import APIView, Response
from django.views.generic.edit import CreateView

from .models import User, Faces, Visitors
from .serializers import UserSerializer, FacesSerializer, VisitorsSerializer

import os
import requests
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = BASE_DIR+"/media"
VISITOR_DIR = MEDIA_DIR+"/visitors"

class UserView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        queryset=User.objects.all()
        items = UserSerializer(queryset, many=True)
        return Response(items.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacesView(APIView):
    serializer_class = FacesSerializer

    def get(self, request):
        queryset=Faces.objects.all()
        items = FacesSerializer(queryset, many=True)
        return Response(items.data)
    def post(self, request):
        folderSet = Visitors.objects.get(pk=request.data['folderName'])
        folderObject = VisitorsSerializer(folderSet)
        fileName = os.path.join(MEDIA_DIR+"/visitors/"+folderObject['visitorName'].value, "face.jpg")
        file = request.FILES['photo']
        path = default_storage.save(fileName, ContentFile(file.read()))
        file.close()

        serializer = FacesSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        queryset = Faces.objects.all()
        queryset.delete()

class VFaceView(APIView):
    serializer_class = FacesSerializer

    def get(self, request, visitorname):
        arr = []
        for file in os.listdir(VISITOR_DIR+'/'+visitorname):
            if file.endswith(".jpg"):
                print(file.title())
                arr.append(VISITOR_DIR+'/'+visitorname+'/'+file.title())
        return Response(arr)

class VisitorsView(APIView):
    serializer_class = VisitorsSerializer

    def get(self, request):
        queryset=Visitors.objects.all()
        items = VisitorsSerializer(queryset, many=True)
        return Response(items.data)
    def post(self, request):
        VISITOR_DIR = MEDIA_DIR+"/visitors/"+request.data['visitorName']
        os.mkdir(VISITOR_DIR)
        serializer = VisitorsSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        queryset = Visitors.objects.all()
        queryset.delete()