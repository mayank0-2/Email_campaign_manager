
from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTING_MODULE', 'Email_campaign_manager.settings')

#Configuration of celery is done here

app = Celery('Email_campaign_manager')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)
