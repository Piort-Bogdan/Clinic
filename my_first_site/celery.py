import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_site.settings')

app = Celery('my_first_site')

app.config_from_object('django.conf:settings', namespace='CELERY')

#Celery будет автоматически искать асинхронные задачи в проекте
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)