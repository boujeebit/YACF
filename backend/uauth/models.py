from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    team = models.ForeignKey(Team, default=None, null=True, blank=True, related_name='players', on_delete=models.SET_NULL)
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username