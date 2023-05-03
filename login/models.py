from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group

user_group, created = Group.objects.get_or_create(name="Users")
maint_group, created = Group.objects.get_or_create(name="Maintenance")
# Create your models here.
class userRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roleStatus = models.IntegerField()
