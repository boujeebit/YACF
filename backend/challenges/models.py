from django.db import models
from categories.models import Category

class Challenge(models.Model):
    # TODO: REMOVE delete on cascade! We may not want to delete all the challenges too
    category = models.ForeignKey(Category, default=None, null=True, on_delete=models.CASCADE, related_name='challenges')

    name = models.CharField(max_length=25)
    description = models.CharField(max_length=1000)

    points = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Flag(models.Model):
    challenge = models.OneToOneField(Challenge, on_delete=models.CASCADE, related_name='flag')
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.challenge.name

class Hint(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='hint')

    content = models.CharField(max_length=1000)
    hidden = models.BooleanField(default=True)

    def __str__(self):
        return self.challenge.name