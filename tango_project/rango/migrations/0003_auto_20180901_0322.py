# Generated by Django 2.0.5 on 2018-09-01 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20180825_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]