# Generated by Django 4.2.8 on 2023-12-09 21:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diaryapp', '0003_alter_entry_entry_content_alter_entry_entry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
