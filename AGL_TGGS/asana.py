#!python
import requests
import json

from AGL_TGGS.models import Project, Job
from django.contrib.auth.models import User


# PAT
headers = {'Authorization': 'Bearer 0/ea4e1acbc8e9d9ef9cc2e2cd625f2db8'}

# Get projects
p_url = "https://app.asana.com/api/1.0/projects?opt_fields=id,created_at,due_date,current_status,members.id,members.name,name&workspace=510975529506053"
p = requests.request("GET", p_url, headers=headers)
projects = p.json()
for project in projects['data']:
    case = Project(
         title=project['name'], 
         start_date=project['created_at'][0:10])
    case.save()

# Get tasks
for i in projects['data']:
    t_url = "https://app.asana.com/api/1.0/tasks?opt_fields=created_at,name,completed,completed_at,due_on,projects.name,tags.name,assignee.name&project=%s"%(i['gid'])
    t = requests.request("GET", t_url, headers=headers)
    tasks = t.json()
    for task in tasks['data']:
        if task['assignee'] is not None:
            job = Job(
                content=task['name'], 
                completed=task['completed'], 
                assignee=task['assignee']['name'])
            job.save()
        else:
            pass
