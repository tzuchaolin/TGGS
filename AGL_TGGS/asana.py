#!python
import re
import requests
import json

from django.contrib.auth import get_user_model
from AGL_TGGS.models import Project, Job, Assignee


# PAT
headers = {'Authorization': 'Bearer 0/ea4e1acbc8e9d9ef9cc2e2cd625f2db8'}
asana_url = 'https://app.asana.com/api/1.0'
workspace_gid = '510975529506053'


# Get Users
users_url = f'{ asana_url }/users?opt_fields=email'
resp = requests.request("GET", users_url, headers=headers).json()['data']

for asana_user in resp:
    assignee = Assignee.objects.filter(gid=asana_user['gid']).first()
    if not assignee:
        asana_email = asana_user['email']
        user = get_user_model().objects.filter(email=asana_email).first()
        if user:
            Assignee.objects.create(user=user, gid=asana_user['gid'])
   

# Get tasks 
for assignee in Assignee.objects.all():
    assignee_tasks_url = f'{ asana_url }/tasks?workspace={ workspace_gid }&assignee={ assignee.gid }&opt_fields=assignee,completed,tags.name,name'
    resp = requests.request("GET", assignee_tasks_url, headers=headers).json()['data']

    for task in resp:
        
        # Create projects
        project = None
        tags = task['tags']
        for tag in tags:
            name = tag['name']
            g_pattern = re.compile(r'^g(\d)+-(\d)+-(\d)+@')
            g_match = g_pattern.match(name)
            a_pattern = re.compile(r'^a(\d)+_(\d)+_(\d)+_(\w)+@')
            a_match = a_pattern.match(name)

            if g_match:
                project = Project.objects.filter(title=name).first()
                if not project:
                    project = Project.objects.create(gid=tag['gid'], title=tag['name'])
            if a_match:
                project = Project.objects.filter(title=name).first()
                if not project:
                    project = Project.objects.create(gid=tag['gid'], title=tag['name'])

        job = Job.objects.filter(gid=task['gid']).first()
        if not job:
            Job.objects.create(gid=task['gid'],
                               completed=task['completed'],
                               content=task['name'],
                               assignee=assignee,
                               project=project)
       

#Get grade from tasks
for task in Job.objects.all():
    name = task.content
    pattern = re.compile(r'\$+\d+\.?\d*p$', re.IGNORECASE)
    match = pattern.search(name)
    if match and task.completed is True:
        point = re.search(r'\d+\.?\d*', match.group(0))
        Job.objects.filter(content=name).update(grade=point.group(0))

for assignee in Assignee.objects.all():
    point = 0
    for job in Job.objects.filter(assignee_id=assignee.id).all():
        point += job.grade
    Assignee.objects.filter(gid=assignee.gid).update(sum_grade=point)