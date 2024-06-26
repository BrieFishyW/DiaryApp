# Generated by Django 4.2.8 on 2023-12-09 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0002_entry_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_content',
            field=models.TextField(default='', max_length=100000),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_date',
            field=models.DateField(default=datetime.date(2023, 12, 9)),
        ),
        migrations.AlterField(
            model_name='entry',
            name='entry_title',
            field=models.CharField(default='December 09, 2023', max_length=100),
        ),
    ]
