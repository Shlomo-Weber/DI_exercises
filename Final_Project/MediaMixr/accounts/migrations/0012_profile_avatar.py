# Generated by Django 3.0.4 on 2020-04-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200331_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='media/avatar.jpeg', upload_to='media'),
        ),
    ]
