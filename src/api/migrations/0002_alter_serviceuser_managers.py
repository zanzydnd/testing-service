# Generated by Django 3.2.6 on 2021-08-17 12:55

import api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='serviceuser',
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
    ]