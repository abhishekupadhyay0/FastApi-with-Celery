from celery import Celery


celery_app = Celery('worker',
                    broker='amqp://guest@localhost//',
                    backend='amqp',
                    include=['worker.celery_task'])


celery_app.conf.task_default_queue = 'default-queue'
celery_app.conf.task_routes = {"worker.celery_task.demo_task": "demo-queue",
                               "worker.celery_task.demo_subtract_task": "demo-subtract-queue"}
celery_app.conf.update(task_track_started=True, result_expires=3600)
