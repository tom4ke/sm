# Generated by Django 3.0.1 on 2020-02-11 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moderators', '0003_moderator_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderator',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]