# Generated by Django 2.2.5 on 2020-02-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_At',
            field=models.DateTimeField(),
        ),
    ]