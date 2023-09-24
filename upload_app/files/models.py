import os
from datetime import datetime
from django.db import models


def upload_to(instance, filename):
    now = datetime.now()
    base, extension = os.path.splitext(filename.lower())
    return f"{base}_{now:%H%M%S}{extension}"


class UploadFile(models.Model):
    file = models.FileField(verbose_name="Файл", upload_to=upload_to)
    uploaded_at = models.DateTimeField(
        verbose_name="Дата и время загрузки", auto_now=True
    )
    processed = models.BooleanField(verbose_name="Файл обработан", default=False)

    def __str__(self) -> str:
        return f"{self.file}"
