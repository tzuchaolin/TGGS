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
        job = Job.objects.filter(gid=task['gid']).first()
        if not job:
            Job.objects.create(gid=task['gid'],
                               completed=task['completed'],
                               content=task['name'],
                               assignee=assignee)
        # Create projects
        tags = task['tags']
        for tag in tags:
            name = tag['name']
            pattern = re.compile(r'^g(\d)+_(\d)+_(\d)-')
            match = pattern.match(name)
            if match:
                project = Project.objects.filter(title=name).first()
                if not project:
                    Project.objects.create(gid=tag['gid'], title=tag['name'])
