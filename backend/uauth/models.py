from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Competitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)