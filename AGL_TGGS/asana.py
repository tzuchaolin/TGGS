import requests
import json


# PAT
headers = {'Authorization': 'Bearer 0/ea4e1acbc8e9d9ef9cc2e2cd625f2db8'}

# Get projects
p_url = "https://app.asana.com/api/1.0/projects?opt_fields=id,created_at,due_date,\
        current_status,members.id,members.name,name&workspace=510975529506053"
payload = {}

p = requests.request("GET", p_url, headers=headers, data = payload)
projects = p.json()

# Get tasks
for i in projects['data']:
    t_url = "https://app.asana.com/api/1.0/tasks?opt_fields=created_at,name,notes,\
            completed,completed_at,due_at,projects.name,tags,followers.name\
            &project=%s"%(i['gid'])

    t = requests.request("GET", t_url, headers=headers, data = payload)
    tasks = t.json()

    print(json.dumps(tasks, indent=4, ensure_ascii=False))
    '''with open('data.txt', 'a+', encoding="utf-8") as outfile:
        json.dump(tasks, outfile, indent=4, ensure_ascii=False)'''