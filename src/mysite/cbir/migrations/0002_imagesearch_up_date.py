# Generated by Django 4.1.2 on 2023-11-13 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbir', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesearch',
            name='up_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 13, 17, 1, 22, 733325, tzinfo=datetime.timezone.utc)),
        ),
    ]
