# Generated by Django 3.1.5 on 2021-02-09 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subjects',
        ),
    ]
