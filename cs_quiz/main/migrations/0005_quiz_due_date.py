# Generated by Django 3.2.8 on 2021-10-30 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211023_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 30, 15, 44, 5, 821965, tzinfo=utc)),
            preserve_default=False,
        ),
    ]