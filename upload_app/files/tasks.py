import time
from celery import Celery, Task


app = Celery("tasks")  # TODO подтянуть из settings.py


@app.task()
def file_processing(data):
    print("processing...", data.get("file"))
    time.sleep(5)
    return data
