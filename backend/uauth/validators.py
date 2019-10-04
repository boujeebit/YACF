from django.conf import settings

import re
from uauth.models import User

def validate_username(value):
    if not re.match(r"^[a-zA-Z0-9_\s]{1,150}$", value):
        raise Exception("Username invalid")

def validate_user_is_authenticated(user):
    if user.is_anonymous:
        raise Exception('Not authorized to see superuser information.')

def validate_user_is_admin(user):
    validate_user_is_authenticated(user)
    if not user.is_superuser:
        raise Exception('Administrator permission required')

def validate_user_is_staff(user):
    if user.is_superuser or user.is_staff:
        return True
    else:
        return False

def validate_username_unique(value):
    if User.objects.filter(username__iexact=value).exists():
        raise Exception('Username not available')

def validate_email(value):
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
        raise Exception("Email invalid")

def validate_email_unique(value):
    if User.objects.filter(email__iexact=value).exists():
        raise Exception('Email already registered')


def validate_password(value):
    if not re.match(r"^[a-zA-Z0-9\ \!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]{12,}$", value):
        raise Exception('Password invalid. Must contain an uppercase letter, lowercase letter, a digit, a special character and be at least 12 characters long')

def authenticate(username=None, password=None):
    login_valid = (settings.ADMIN_LOGIN == username)
    pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
    if login_valid and pwd_valid:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        return user
    return None