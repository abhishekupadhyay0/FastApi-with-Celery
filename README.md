# FastApi-with-Celery
This project is for async processing of fastapi requests through celery workers.

1. Creating a FastApi to accept 2 numbers for addition and subtraction (main.py). The endpoints will be /add & /subtract. Asynchronous result can be requested at /result. Once a request is made on any endpoint, a UUID will be returned as an acknowledgement. This acknowledge string or UUID can be used to get the result once processing is over.
2. Creating a Celery App module inside worker directory (celery_app.py). First we will initialize the celery application with parameters a) project name, b) RabbitMQ broker URL, c) backend AMQP or Redis and d) include param (file name where celery tasks are defined).
3. Creating a celery task file which has 2 functions (celery_tasks.py). these functions will add and subtract the numbers.

# Installations required for development
Celery, Fastapi, Uvicorn, RabbitMQ, Flower

# Commands to run application:
Below are the commands to run fastapi and celery workers

1. Fast API application: uvicorn main:app --reload

2. Celery worker: celery worker -A worker.celery_task -l info -c 1 -Q demo-queue
                  celery worker -A worker.celery_task -l info -c 1 -Q demo-subtract-queue
                  
3. Flower: flower -A worker.celery_task --address=127.0.0.1 --port=5555

# Testing

Open SwaggerUI on http://127.0.0.1:8000/docs and try the addition API. pass 2 numbers in the request and you will get an UUID.
Use that UUID and call results api by passing UUID in the request. You will see the result in response.
