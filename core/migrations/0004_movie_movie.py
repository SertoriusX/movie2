# Generated by Django 5.0.2 on 2024-02-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_movie_description_movie_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]