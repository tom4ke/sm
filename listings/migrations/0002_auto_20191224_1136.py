# Generated by Django 3.0.1 on 2019-12-24 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='user',
            new_name='account',
        ),
    ]
