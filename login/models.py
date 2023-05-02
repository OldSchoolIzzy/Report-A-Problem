from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.
class userRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roleStatus = models.IntegerField()
