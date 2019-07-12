from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=25)
    primary = models.CharField(max_length=8)
    secondary = models.CharField(max_length=8)
    foucs = models.CharField(max_length=8)
    accent = models.CharField(max_length=8)

    def __str__(self):
        return self.name