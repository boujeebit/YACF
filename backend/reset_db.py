import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Imports
import argparse, contextlib
import json
from django.utils import timezone
from datetime import timedelta
from core.settings import DATABASES
from django.contrib.auth.models import User
from uauth.models import Profile
from teams.models import Team, AccessCode
from categories.models import Category
from challenges.models import Challenge, Flag
from uauth.validators import validate_username, validate_password, validate_email

from random import randint
import hashlib

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
    admin = User.objects.create_superuser("admin", "email@email.com", "password1", first_name="Admin", last_name="Admin")
    admin.save()
    profile = Profile(user=admin, verified=True)
    profile.save()

def makeTeam(team_name, hidden, accesscode):
    team = Team(name=team_name, hidden=hidden)
    team.save()
    AccessCode(team=team, value=accesscode).save()

    return team

def makeUser(user_name, user_email, user_password, user_team, hidden):
    # Validate admin user command line arguments
    validate_username(user_name)
    validate_email(user_email)
    validate_password(user_password)

    # Create team for admin user
    # user_team = Team(name=user_name, hidden=hidden)
    # user_team.save()

    user = User(username=user_name, email=user_email, first_name=user_name, last_name=user_name)
    user.set_password(user_password)
    user.save()

    profile = Profile(user=user, verified=True, team=user_team, hidden=hidden)
    profile.save()

def makeCategories():
    ctf_categories = ['Web', 'Pwn', 'Crypto', 'Reverse', 'Triva', 'Script']

    for category in ctf_categories:
        cat = Category(name=category, description="%s challenges" % (category))
        cat.save()

def makeChallenges():
    ctf_categories = ['Web', 'Pwn', 'Crypto', 'Reverse', 'Triva', 'Script']
    ctf_challenge_points = [100, 200, 300, 400, 500]

    for category in ctf_categories:
        cat = Category.objects.get(name=category)
        for challenge_points in ctf_challenge_points:
            chal_str = "%s %s" % (category, str(challenge_points))
            chal = Challenge(category=cat, name=chal_str, description="{0} challenge".format(chal_str), points=challenge_points, hidden=True)
            chal.save()
            flag = Flag(value=hashlib.md5('flag'.encode('utf-8')).hexdigest(), challenge=chal)
            flag.save()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YACF database reset script')
    parser.add_argument('--name', action="store", dest="admin_name", help='Username of admin user', default="admin")
    parser.add_argument('--email', action="store", dest="admin_email", help='Email of admin user', default="admin@yacf.com")
    parser.add_argument('--password', action="store", dest="admin_password", help='Password of admin user', default="Password123!")
    parser.add_argument('--categories', action="store", dest="create_categories", help='Flag to create categories')
    parser.add_argument('--challenges', action="store", dest="create_challenges", help='Flag to create challenges')

    args = parser.parse_args()

    # Rest the django database
    resetDjangoDB()

    # Make the admin user
    # makeAdminUser(args.admin_name, args.admin_email, args.admin_password, True)
    makeAdminUser()

    #Create some teams
    team1 = makeTeam("Team1", False, "abc")
    team2 = makeTeam("Team2", False, "abc")
    team3 = makeTeam("Team3", False, "abc")
    team4 = makeTeam("Team4", False, "abc")
    team5 = makeTeam("Team5", False, "abc")

    # Create some player users
    makeUser("user1", "user1@yactf.com", "Password123!", team1, True)
    makeUser("user2", "user2@yactf.com", "Password123!", team2, True)
    makeUser("user3", "user3@yactf.com", "Password123!", team3, True)
    makeUser("user4", "user4@yactf.com", "Password123!", team4, True)
    makeUser("user5", "user5@yactf.com", "Password123!", team5, True)

    # Create challenge categories if requested
    # if args.create_categories:
    makeCategories()

    # Create challenges if requested
    # if args.create_challenges:
    makeChallenges()