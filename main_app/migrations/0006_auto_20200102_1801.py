# Generated by Django 2.2.6 on 2020-01-02 18:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200102_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datePublished',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 2, 18, 1, 38, 257699, tzinfo=utc)),
        ),
    ]