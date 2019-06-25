from rest_framework import serializers
from .models import User, Visitors, Faces

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password')

class VisitorsSerializer(serializers.ModelSerializer):
	class Meta:
		owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
		model = Visitors
		fields = ('id', 'owner','visitorName')

class FacesSerializer(serializers.ModelSerializer):
	class Meta:
		folderName = serializers.PrimaryKeyRelatedField(queryset=Visitors.objects.all())
		model = Faces
		fields = ('id', 'photo', 'folderName')