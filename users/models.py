from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    suer = models.OneToOneField(User, on_delete=models.CASCADE)

# Create your models here.
