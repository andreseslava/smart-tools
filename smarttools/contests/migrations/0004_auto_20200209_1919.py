# Generated by Django 3.0.2 on 2020-02-10 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_auto_20200209_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 9, 19, 19, 38, 384346)),
        ),
        migrations.AlterField(
            model_name='contest',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 9, 19, 19, 38, 384346)),
        ),
    ]
