# Generated by Django 3.0.4 on 2020-03-31 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200331_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]