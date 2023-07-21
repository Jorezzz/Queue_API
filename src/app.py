import fastapi
from celery_worker import add_two, celery
from celery.result import AsyncResult

app = fastapi.FastAPI()

@app.get("/")
async def hello_world():
    return {"Hello": "World 123"}

@app.get("/add/{x}/{y}")
async def add(x: int, y: int):
    task = add_two.delay(x, y)
    return {"taskid": task.id}

@app.get("/task/{taskid}")
async def task(taskid: str):
    result = AsyncResult(taskid, app=celery)
    if result.state == 'SUCCESS':
        return {"state": result.state, "result": result.get()}
    else:
        return {"state": result.state, "result": None}