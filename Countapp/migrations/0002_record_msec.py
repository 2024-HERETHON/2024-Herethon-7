# Generated by Django 5.0.3 on 2024-06-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Countapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='msec',
            field=models.IntegerField(default=0),
        ),
    ]
