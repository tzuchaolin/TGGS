#!python
from AGL_TGGS import asana
from django_cron import CronJobBase, Schedule


# Cron
class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'AGL_TGGS.my_cron_job'

    def do(self):
        exec(open('asana.py').read())
