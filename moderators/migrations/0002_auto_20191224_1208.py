# Generated by Django 3.0.1 on 2019-12-24 12:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moderators', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moderator',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='moderator',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
