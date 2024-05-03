from django.db import models
from datetime import datetime

class Todo(models.Model):
    todo=models.TextField()
    name=models.CharField(max_length=30)