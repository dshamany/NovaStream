# Generated by Django 2.2.6 on 2020-01-02 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20200102_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datePublished',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
