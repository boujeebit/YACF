from django.db import models

# TODO: On delete? What happens to the challenges?
class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=1000)
    
    hidden = models.BooleanField(default=False) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name