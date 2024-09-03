from django.contrib import admin
from .models import ProjectLink

@admin.register(ProjectLink)
class ProjectLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')