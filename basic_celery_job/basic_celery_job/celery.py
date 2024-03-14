import os

from celery import Celery
from django.conf import settings
from datetime import timedelta
from .tasks import scrape_proxies

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_celery_job.settings')

app = Celery('basic_celery_job.celery')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

CELERY_ACCEPT_CONTENT = ['application/json', 'pickle']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'
CELERY_TASK_TIME_LIMIT = 10 * 60
CELERY_TASK_SOFT_TIME_LIMIT = 9 * 60

# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(timedelta(days=1), scrape_proxies.s())
