from django.contrib import admin
from .models import Team, SolvedChallenge

admin.site.register(Team)
admin.site.register(SolvedChallenge)

# class solvedValueInline(admin.TabularInline):
#     model = 