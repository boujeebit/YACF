from django.db import models
from challenges.models import Challenge

# Create your models here.
class SolvedChallenge(models.Model):
    """
    Team solved challenge model
    TODO: Add what user solved the challenge on the team
    """
    challenge = models.ForeignKey(Challenge, default=None, null=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Team(models.Model):
    """
    Team model class.
    """
    name = models.CharField(max_length=150, unique=True)
    points = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)
    #TODO: May not be need. Should be the same as len(solved). Could do it in def
    correct_flags = models.IntegerField(default=0)
    wrong_flags = models.IntegerField(default=0)
    #TODO: Come back to this Many to Many - Solved challenge should link to team to avoid issues
    solved = models.ManyToManyField(SolvedChallenge)
    created = models.DateTimeField(auto_now_add=True)

    accesscode = models.CharField(max_length=150)