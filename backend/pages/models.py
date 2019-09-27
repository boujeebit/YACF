from django.db import models

class Page(models.Model):
    """
    Page model
    """
    url     = models.CharField(max_length=15, unique=True)
    name    = models.CharField(max_length=15)
    content = models.CharField(max_length=5000)
    authenticated = models.BooleanField(default=True)

    def __str__(self):
        return self.name