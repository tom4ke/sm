# Generated by Django 3.0.1 on 2019-12-24 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderators', '0002_auto_20191224_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='moderator',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]