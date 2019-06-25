from rest_framework import viewsets,status
from rest_framework.views import APIView, Response
from django.views.generic.edit import CreateView

from .models import User, Faces, Visitors
from .serializers import UserSerializer, FacesSerializer, VisitorsSerializer

import os

# from datetime import datetime, date, timedelta
# import random
# import time
# import csv
# import pandas as pd
# import numpy as np
# import json
# import copy
# from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
# from django.utils.timezone import make_aware
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = BASE_DIR+"/media"

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
        fileName = os.path.join(MEDIA_DIR+"/visitors/"+folderObject['visitorName'].value, "Peter1.jpg")
        fileF = os.open(fileName, 'w')
        fileF.write(request.data['photo'])
        fileF.close()
        serializer = FacesSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        queryset = Faces.objects.all()
        queryset.delete()

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