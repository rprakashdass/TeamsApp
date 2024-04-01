from django.contrib import admin
from .models import Task, Team, Contributor, Project

admin.site.register(Task)
admin.site.register(Team)
admin.site.register(Contributor)
admin.site.register(Project)