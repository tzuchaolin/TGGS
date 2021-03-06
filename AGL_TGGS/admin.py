from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from AGL_TGGS.models import Project, Job


# @admin.register(Cost)
# class CostAdmin(admin.ModelAdmin):
#     list_display = ('project', 'content', 'amount')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'start_date', 'deadline', 'end_date', 
                    'budget')
    
    # def grade(self, obj):
    #     return obj.grade()
    
    # grade.short_description = "Grade"


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('content', 'assignee', 'completed')
    list_filter = ('assignee', 'completed')