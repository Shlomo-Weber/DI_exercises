# Generated by Django 3.0.6 on 2020-05-12 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20200401_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 12, 12, 24, 29, 160795)),
        ),
    ]
