# Generated by Django 3.0.4 on 2020-03-25 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
        ('accounts', '0003_book_movie_tv_show_video_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recommendation.Genre'),
        ),
    ]
