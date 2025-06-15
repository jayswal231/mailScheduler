import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailScheduler.settings')

app = Celery('mailScheduler')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()