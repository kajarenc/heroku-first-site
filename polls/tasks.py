import random
from mysite.celery import app


@app.task(bind=True)
def add(x, y):
    return x + y

@app.task(bind=True)
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total

@app.task(bind=True)
def xsum(numbers):
    return sum(numbers)