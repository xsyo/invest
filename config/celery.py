import os

import dotenv
from celery import Celery

dotenv.read_dotenv()

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'update_balance': {
        'task': 'packages.tasks.update_balance',
        'schedule': 15.0
    }
}


# Celery command
# celery -A config beat
# celery -A config worker -l INFO [--pool=solo]