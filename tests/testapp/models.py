from django.db import models


class TestModel(models.Model):
    date_time_1 = models.DateTimeField()
    date_time_2 = models.DateTimeField()
