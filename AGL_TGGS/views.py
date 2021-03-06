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

def project(request, project_gid):
    project = Project.objects.get(gid=project_gid)
    
    division = {}

    jobs = project.job_set.all()
    for job in jobs:
        if job.assignee in division.keys():
            division.setdefault(job.assignee, []).append(job)            
        else:
            division[job.assignee] = [job]

    context = {
        'division': division,
    }

    return render(request, 'AGL_TGGS/division.html', context)