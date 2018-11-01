from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

