from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Visitors(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    visitorName = models.CharField(max_length=100)

class Faces(models.Model):
    folderName = models.ForeignKey(Visitors, on_delete=models.CASCADE)
    photo = models.ImageField()