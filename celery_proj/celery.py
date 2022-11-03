import os

from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_proj.settings')

app = Celery('celery_proj')

#disable utc(Universal timezone)
app.conf.enable_utc = False

#change Timezone of celery to Asia/Kolkata
app.conf.update(timezone = 'Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

#Scheduler of tasks
# app.conf.beat_schedule = {
#     'mail_scheduler':{
#         'task':'celery_app.task.send_an_email',
#         'schedule': crontab(),
#         # 'schedule': crontab(hour='*', minute=5),
#         'args': ('TestCase','This is Test Email',*["patelmanthan2905@gmail.com"])
#     }
# } 


# Load task modules from all registered Django apps.
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')