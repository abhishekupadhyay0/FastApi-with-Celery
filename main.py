from celery.bin.result import result
from celery.task import task
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

from worker import celery_task
from worker.celery_app import celery_app

# Create the FastAPI app
app = FastAPI()


class Numbers(BaseModel):
    x: float
    y: float


class Result(BaseModel):
    status: str
    data: str
    error: str


def on_message(response):
    print(response)


@app.post('/add')
async def enqueue_add(n: Numbers, background_task: BackgroundTasks):
    # We can use celery delay method in order to enqueue the task with the given parameters
    # response = demo_task.delay(n.x, n.y)
    response = celery_app.send_task("worker.celery_task.demo_task", args=(n.x, n.y), queue='demo-queue')
    background_task.add_task(on_message, response)
    return {"acknowledgement": str(response)}


@app.post('/subtract')
async def enqueue_subtract(n: Numbers, background_task: BackgroundTasks):
    # We can use celery delay method in order to enqueue the task with the given parameters
    # response = demo_subtract_task.delay(n.x, n.y)
    response = celery_app.send_task("worker.celery_task.demo_subtract_task", args=(n.x, n.y), queue='demo-subtract'
                                                                                                    '-queue')
    background_task.add_task(on_message, response)
    return {"acknowledgement": str(response)}


@app.post('/result')
async def enqueue_result(ack: str):
    task_result = celery_app.AsyncResult(ack)
    if task_result.ready():
        return {"status": task_result.status,
                "data": task_result.get()}
    return {"status": task_result.status,
            "data": 0}
