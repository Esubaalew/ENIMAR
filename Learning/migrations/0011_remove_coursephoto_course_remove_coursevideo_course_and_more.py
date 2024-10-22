# Generated by Django 5.0 on 2024-01-26 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Learning', '0010_rename_assessment_quiz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursephoto',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursevideo',
            name='course',
        ),
        migrations.RemoveField(
            model_name='file',
            name='course',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='course',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='course',
        ),
        migrations.AlterField(
            model_name='course',
            name='poster',
            field=models.ImageField(help_text='An image representing the course', upload_to='learning/course/posters/'),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='Learning.course')),
            ],
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsections', to='Learning.section')),
            ],
        ),
        migrations.AddField(
            model_name='coursephoto',
            name='subsection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='Learning.subsection'),
        ),
        migrations.AddField(
            model_name='coursevideo',
            name='subsection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='Learning.subsection'),
        ),
        migrations.AddField(
            model_name='file',
            name='subsection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='Learning.subsection'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='subsection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='Learning.subsection'),
        ),
        migrations.AddField(
            model_name='reading',
            name='subsection',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='Learning.subsection'),
        ),
    ]
