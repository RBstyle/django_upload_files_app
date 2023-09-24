import time
from celery import Celery
from typing import NoReturn

from files.models import UploadFile

app = Celery("tasks")


@app.task()
def file_processing(file_id: int, file_type: str) -> NoReturn:
    """Задача по обработке файлов
    ---
    Аргументы:

    file_id - ID файла

    file_type - тип файла(image, audio, text, video)
    """
    # имитация обработки разных типов файлов. Значениями в словаре могут быть соответствующие функции.
    processing = {
        "image": f"processing image file ID:{file_id}",
        "audio": f"processing audio file ID:{file_id}",
        "text": f"processing text file ID:{file_id}",
        "video": f"processing video file ID:{file_id}",
    }

    print(processing[file_type])

    time.sleep(10)  # имитация работы задачи

    # Изменение статуса(processed) файла
    instance = UploadFile.objects.get(pk=file_id)
    instance.processed = True
    instance.save()

    print(f"Done! File ID:{file_id}")
