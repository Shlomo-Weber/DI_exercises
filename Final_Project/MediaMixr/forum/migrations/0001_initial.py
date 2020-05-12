# Generated by Django 3.0.4 on 2020-03-30 12:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0007_auto_20200326_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField(null=True)),
                ('pubdate', models.DateTimeField(default=datetime.datetime(2020, 3, 30, 12, 27, 50, 863275))),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Media')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
