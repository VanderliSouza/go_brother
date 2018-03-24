from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, blank=True)
    autor = models.TextField(max_length=255, blank=True)
    in_print = models.BooleanField(default=True)
    image = models.FileField(upload_to='documents/%Y,%m,%d', null=True, blank=True)


def __str__(self):
    return self.title
