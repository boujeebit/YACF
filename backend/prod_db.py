import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import argparse, contextlib
import json
from django.utils import timezone
from datetime import timedelta
from core.settings import DATABASES
from django.contrib.auth.models import User
from uauth.models import Profile


def resetDjangoDB():
    # Remove database file if exists
    with contextlib.suppress(FileNotFoundError):
        os.remove(DATABASES['default']['NAME'])
    
    # Remove migrations
    os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
    os.system('find . -path "*/migrations/*.pyc"  -delete')

    # Rebuild database
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate')   

def makeAdminUser():
    admin = User.objects.create_superuser("admin", "email@email.com", "yacfadmin")
    admin.first_name = "Admin"
    profile = Profile(user=admin, verified=True, hidden=True)
    admin.save()
    profile.save()

if __name__ == "__main__":
    # Rest the django database
    resetDjangoDB()

    # Make the admin user
    makeAdminUser()

    #Make welcome page