from datetime import date

from django.db import models
from django.utils import timezone


# Create your models here.
class Entry(models.Model):
    entry_title = models.CharField(max_length=100, default=date.today().strftime("%B %d, %Y"))
    entry_content = models.TextField(max_length=100000, default="")
    entry_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.entry_title
