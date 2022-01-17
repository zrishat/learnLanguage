import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learnLanguage.settings')

app = Celery('english')
app.config_from_object('django.conf:settings', namespace='english')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
