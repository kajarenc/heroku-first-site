import random
from mysite.celery import app


@app.task(bind=True)
def add(self, x, y):
    return x + y

@app.task(bind=True)
def mul(self, x, y):
    total = x * (y * random.randint(3, 100))
    return total

@app.task(bind=True)
def xsum(self, numbers):
    return sum(numbers)