# Generated by Django 5.0 on 2023-12-30 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='courses_created',
        ),
    ]
