# Generated by Django 2.2.6 on 2020-01-02 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200102_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='datePublished',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
