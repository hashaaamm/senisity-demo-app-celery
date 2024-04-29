"""
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
"""
import os

from celery import Celery

from django.conf import settings

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# you can change the name here
app = Celery("mysite")

app.conf.broker_connection_retry_on_startup = True

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# discover and load tasks.py from from all registered Django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def divide(x, y):
    import time
    try:
        # Simulate a long-running task
        time.sleep(5)
        result = x / y
        return result
    except Exception as e:
        # Log the exception
        app.logger.error("Error occurred during task execution: %s", str(e))
        # Return a default value or raise the exception if appropriate
        return None


