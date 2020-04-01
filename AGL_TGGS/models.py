import time
from django.db import models
from functools import reduce
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Assignee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gid = models.CharField(max_length=50)
    sum_grade = models.FloatField(max_length=20, default=0)
    

class Project(models.Model):
    # details
    gid = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    start_date = models.DateField(null=True)
    deadline = models.DateField(null=True)
    end_date = models.DateField(null=True)
    budget = models.IntegerField(null=True)
    
    # modified datetime
    created_at = models.DateTimeField('created at', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return self.title


class Job(models.Model):
    # relations
    assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    # details
    gid = models.CharField(max_length=50)
    content = models.CharField(max_length=50, default='')
    completed = models.BooleanField(default=False)
    grade = models.FloatField(max_length=20, default=0)

    def __str__(self):
        return self.content
    