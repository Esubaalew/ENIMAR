# Generated by Django 5.0 on 2024-01-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0003_alter_course_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='poster',
            field=models.ImageField(help_text='An image representing the course', upload_to='Learning/static/images/posters/'),
        ),
    ]
