from django.contrib import admin
from .models import ProjectLink, Name

@admin.register(ProjectLink)
class ProjectLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('name',)