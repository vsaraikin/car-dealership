import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_dealership.settings')

app = Celery('car_dealership')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'supplier_to_dealer_task': {
        'task': 'car_dealership.tasks.supplier_to_dealer_task',
        'schedule': 10.0
    },
    'dealer_to_buyer_task': {
        'task': 'car_dealership.tasks.dealer_to_buyer_task',
        'schedule': 10.0
    }
}
