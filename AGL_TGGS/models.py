import time
from django.db import models
from functools import reduce
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):
    # relations
    member = models.ManyToManyField(User)

    # details
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    start_date = models.DateField(blank=True)
    deadline = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    budget = models.IntegerField(blank=True)
    
    # modified datetime
    created_at = models.DateTimeField('created at', auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return self.title


    def display_member(self):
        return ", ".join(member.username for member in self.member.all())

    display_member.short_description = 'Member'

    def grade(self):
        Psalary = 0
        #if len(self.jobdivision_set.all()) > 1:

        if len(self.jobdivision_set.all()) > 1:
            Psalary = reduce(lambda x, y: x.salary + y.salary, self.jobdivision_set.all())
        Sdays = self.end_date - self.deadline
        if Sdays.days > 0:
            cost_of_salary = Sdays.days * Psalary / 30
        else:
            cost_of_salary = 0
        
        cost_of_project = 0
        if len(self.cost_set.all()) > 1:
            cost_of_project = reduce(lambda x, y: x.amount + y.amount, self.cost_set.all())
        return (self.budget - cost_of_project - cost_of_salary) / 1000
    
    '''def grade(self):
        total_cost = reduce(lambda x, y: x.amount + y.amount, self.cost_set) 
        return (self.budget -total_cost) / 1000'''


class Cost(models.Model):
    # relations
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)
    
    # details
    content = models.CharField(max_length=50, null=True)
    amount = models.PositiveIntegerField(null=True, default=0)

    class Meta:
        ordering = ['project']


class JobDivision(models.Model):
    # relations
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=True)

    # details
    ratio = models.PositiveIntegerField(null=True, blank=True, default='', 
                                        validators=[MaxValueValidator(100)])
    salary = models.PositiveIntegerField(null=True)

    def __str__(self):
        worker = str(self.executor)
        return worker


class Job(models.Model):
    # relations
    executor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # details
    content = models.CharField(max_length=200, default='')
    progress = models.BooleanField(default=False)

    def __str__(self):
        return self.content
    
    