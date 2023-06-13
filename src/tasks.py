from src.celery import app


@app.task
def add_numbers(a, b):
    result = a + b
    return result
