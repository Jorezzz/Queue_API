import time
from celery import Celery

celery = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

@celery.task(name = 'add_two')
def add_two(x, y):
    time.sleep(15)
    return x + y