# Generated by Django 3.0.4 on 2020-04-01 08:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200331_1311'),
        ('forum', '0007_auto_20200401_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumcomment',
            name='user',
        ),
        migrations.AddField(
            model_name='forumcomment',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 8, 15, 20, 201686)),
        ),
    ]
