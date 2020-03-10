from django.db import models
from django.contrib.auth.models import User
import datetime


class Project(models.Model):
    title = models.CharField(max_length=200, default='')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    member = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Subject(models.Model):
    ratio = models.FloatField(null=True, blank=True, default='')
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.executor


class Work(models.Model):
    content = models.CharField(max_length=200, default='')
    progress = models.FloatField(null=True, blank=True, default='')