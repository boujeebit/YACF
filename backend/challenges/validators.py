import re
from challenges.models import Challenge

def validate_name(value):
    if not re.match(r"^[a-zA-Z0-9_\s]{1,25}$", value) or Challenge.objects.filter(name__iexact=value).exists():
        raise Exception("Challenge name invalid or already exists")

def validate_description(value):
    if not re.match(r"^[a-zA-Z0-9_\s]{1,1000}$", value):
        raise Exception('Challenge description invalid')

def validate_points(value):
    if value < 0:
        raise Exception('Invalid challenge points value')

def validate_create_flag(value):
    if not re.match(r"^[a-zA-Z0-9\ \!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]{1,100}$", value) or Challenge.objects.filter(flag__iexact=value).exists():
        raise Exception('Invalid flag or flag already exists')

def validate_check_flag(value):
    if not re.match(r"^[a-zA-Z0-9\ \!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~]{1,100}$", value):
        raise Exception('Invalid flag')