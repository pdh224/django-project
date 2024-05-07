from django.db import models


class Todo(models.Model):
    day = models.DateTimeField()
    todo = models.CharField(max_length=30)