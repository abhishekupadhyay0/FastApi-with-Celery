from time import sleep
from .celery_app import celery_app


@celery_app.task(name='worker.celery_task.demo_task', bind=True, acks_late=True)
def demo_task(self, x, y):
    print(f'args', x, y)
    sleep(20)
    result = x + y
    return result


@celery_app.task(name='worker.celery_task.demo_subtract_task', bind=True, acks_late=True)
def demo_subtract_task(self, x, y):
    print(f'args', x, y)
    sleep(1)
    result = x - y
    return result
