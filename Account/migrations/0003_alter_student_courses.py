# Generated by Django 5.0 on 2023-12-30 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_student_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.IntegerField(default=0),
        ),
    ]
