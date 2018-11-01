from django.db import models
from categories.models import Category

class Challenge(models.Model):
    category = models.ForeignKey(Category, default=None, null=True, on_delete=models.CASCADE, related_name='challenges')

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=1000)

    points = models.IntegerField(default=0)
    flag = models.CharField(max_length=100)

    show = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name