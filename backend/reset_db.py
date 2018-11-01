# Hack to use django app models in standalone script
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Imports
import argparse, contextlib
import json
from django.utils import timezone
from datetime import timedelta
from core.settings import DATABASES
from uauth.models import User
from teams.models import Team
from categories.models import Category
from challenges.models import Challenge
from uauth.validators import validate_username, validate_password, validate_email

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

    
def makeAdminUser(admin_name, admin_email, admin_password, hidden):
    # Validate admin user command line arguments
    validate_username(admin_name)
    validate_email(admin_email)
    validate_password(admin_password)

    # Create team for admin user
    admin_team = Team(name=admin_name, hidden=hidden)
    admin_team.save()

    # Create admin user assign admin team
    admin = User.objects.create_superuser(admin_name, admin_email, admin_password)
    admin.team = admin_team
    admin.save()


def makeUser(user_name, user_email, user_password, hidden):
    # Validate admin user command line arguments
    validate_username(user_name)
    validate_email(user_email)
    validate_password(user_password)

    # Create team for admin user
    user_team = Team(name=user_name, hidden=hidden)
    user_team.save()

    user = User(
            username=user_name,
            email=user_email,
            team=user_team,
            hidden=hidden
        )
    user.set_password(user_password)
    user.save()


    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Redctf database reset script')
    parser.add_argument('--name', action="store", dest="admin_name", help='Username of admin user', default="admin")
    parser.add_argument('--email', action="store", dest="admin_email", help='Email of admin user', default="admin@yacf.com")
    parser.add_argument('--password', action="store", dest="admin_password", help='Password of admin user', default="Password123!")

    args = parser.parse_args()

    resetDjangoDB()
    makeAdminUser(args.admin_name, args.admin_email, args.admin_password, True)