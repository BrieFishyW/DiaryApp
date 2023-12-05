from datetime import date

from django.db import models

# Create your models here.
class Entry(models.Model):
    entry_title = models.CharField(max_length=100)
    entry_content = models.TextField(max_length=100000)
    entry_date = models.DateField()

    def __str__(self):
        return self.entry_title
