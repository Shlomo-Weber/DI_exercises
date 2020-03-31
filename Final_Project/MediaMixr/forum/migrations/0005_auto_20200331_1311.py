# Generated by Django 3.0.4 on 2020-03-31 13:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200331_1311'),
        ('forum', '0004_auto_20200331_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='media',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.Media'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='pubdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 31, 13, 11, 32, 654542)),
        ),
    ]
