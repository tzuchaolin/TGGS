from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Project, Subject, Work


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'display_member')
    

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('executor', 'ratio')


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('content', 'progress')