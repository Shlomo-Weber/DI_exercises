# Generated by Django 3.0.4 on 2020-04-01 13:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20200401_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.ForumPost'),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 13, 15, 18, 538349)),
        ),
    ]
