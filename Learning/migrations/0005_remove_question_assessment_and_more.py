# Generated by Django 5.0 on 2024-01-05 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0004_remove_choice_question_question_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='assessment',
        ),
        migrations.RemoveField(
            model_name='question',
            name='correct_choice',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.DeleteModel(
            name='Assessment',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]