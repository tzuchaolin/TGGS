from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AGL_TGGS.models import Project, Job, Assignee


def index(request):
    project_list = Project.objects.order_by('title')
    context = {
        'project_list': project_list,
    }
    return render(request, 'AGL_TGGS/projects.html', context)

def division(request):
    assignee_list = Assignee.objects.order_by('user')
    context = {
        'assignee_list': assignee_list,
    }
    return render(request, 'AGL_TGGS/division.html', context)