from django.db import models


class File(models.Model):
    file = models.FileField(verbose_name="Файл")
    uploaded_at = models.DateTimeField(
        verbose_name="Дата и время загрузки", auto_now=True
    )
    processed = models.BooleanField(verbose_name="Файл обработан", default=False)
