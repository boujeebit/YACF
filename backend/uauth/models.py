from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    team = models.ForeignKey(Team, default=None, null=True, related_name='team', on_delete=models.SET_NULL)
    hidden = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)