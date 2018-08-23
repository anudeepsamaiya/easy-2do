import enum

from django.db import models
from django_extensions.db import models as model_extensions

from commons.models import Category

class Duration(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(unique=True, max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Duration'
        verbose_name_plural = 'Duration'

class Mode(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(unique=True, max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Mode'

class AlertStatus(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(unique=True, max_length=8)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'AlertStatus'
        verbose_name_plural = 'AlertStatuses'


class Alert(model_extensions.TimeStampedModel, model_extensions.ActivatorModel):

    duration = models.IntegerField()
    duration_type = models.ForeignKey(Duration, on_delete=models.PROTECT)
    mode = models.ForeignKey(Mode, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    alert_status = models.ForeignKey(AlertStatus, on_delete=models.PROTECT)

    class Meta:
        abstract = True

    @enum.unique
    class Duration(enum.Enum):
        Hours = 1
        DAYS = 2
        WEEKS = 3
        MONTHS = 4
        YEARS = 5

    @enum.unique
    class Mode(enum.Enum):
        EMAIL = 1
        SMS = 2

    @enum.unique
    class Category(enum.Enum):
        IMPORTANT = 1
        URGENT = 2

    @enum.unique
    class Status(enum.Enum):
        SCHEDULED = 1
        MISSED = 2
