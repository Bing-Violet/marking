from django.db import models
from django.db.models import Min, Max, Avg, StdDev, Count, FloatField
import numpy
# Create your models here.


class Result(models.Model):
    test_id = models.IntegerField()
    scanned_on = models.DateTimeField(null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_number = models.IntegerField()
    mark = models.IntegerField()
