from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vet_clinic_molli.settings')

app = Celery('vet_clinic_molli')

app.config_from_object('django.conf:settings', namespace='CELERY')

#Celery будет автоматически искать асинхронные задачи в проекте
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))