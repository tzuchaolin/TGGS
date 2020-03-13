from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cost, Project, JobDivision, Job

@admin.register(Cost)
class CostAdmin(admin.ModelAdmin):
    list_display = ('project', 'content', 'amount')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'start_date', 'deadline', 'end_date',
                    'display_member', 'budget', 'grade')
    
    def grade(self, obj):
        return obj.grade()
    
    grade.short_description = "Grade"


@admin.register(JobDivision)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('executor', 'ratio', 'salary', 'project')
    list_filter = ('executor', 'project')


@admin.register(Job)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('content', 'executor', 'progress')
    list_filter = ('executor', 'progress')