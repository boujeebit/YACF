import re
from categories.models import Category

def validate_name(value):
    if not re.match(r"^[a-zA-Z0-9_\s]{1,25}$", value) or Category.objects.filter(name__iexact=value).exists():
        raise Exception("Category name invalid or already exists")

def validate_description(value):
    if not re.match(r"^[a-zA-Z0-9_\s]{1,1000}$", value):
        raise Exception('Category invalid')