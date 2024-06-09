# Generated by Django 4.2.13 on 2024-06-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_course'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='payment',
            constraint=models.UniqueConstraint(fields=('user', 'course'), name='unique_user_course_payment'),
        ),
    ]
