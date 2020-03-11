from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Project(models.Model):
    title = models.CharField(max_length=200, default='')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    member = models.ManyToManyField(User)

    def display_member(self):
        return ", ".join(member.username for member in self.member.all())

    display_member.short_description = 'Member'


class Subject(models.Model):
    ratio = models.PositiveIntegerField(null=True, blank=True, default='', 
                                        validators=[MaxValueValidator(100)])
    executor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        worker = str(self.executor)
        return worker


class Work(models.Model):
    content = models.CharField(max_length=200, default='')
    progress = models.FloatField(null=True, blank=True, default='', 
                                 validators=[MinValueValidator(0), MaxValueValidator(100)])