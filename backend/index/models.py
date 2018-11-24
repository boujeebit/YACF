from django.db import models

class WelcomePage(models.Model):
    """
    Welcome page model
    """
    content = models.CharField(max_length=2000)
