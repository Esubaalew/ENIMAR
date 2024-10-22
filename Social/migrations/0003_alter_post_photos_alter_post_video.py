# Generated by Django 5.0 on 2024-01-05 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social', '0002_remove_photo_post_remove_video_post_post_photos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photos',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='Social.photo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Social.video'),
        ),
    ]
