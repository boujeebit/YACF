from django.contrib import admin
from .models import Team, SolvedChallenge, AccessCode

admin.site.register(Team)
admin.site.register(AccessCode)
admin.site.register(SolvedChallenge)