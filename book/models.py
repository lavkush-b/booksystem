import django
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    authors = ArrayField(models.CharField(max_length=255), blank=True)
    country = models.CharField(max_length=255)
    numberOfPages = models.IntegerField(default=0)
    publisher = models.CharField(max_length=255)
    released = models.DateTimeField(default=django.utils.timezone.now)
