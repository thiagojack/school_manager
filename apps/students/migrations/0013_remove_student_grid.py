# Generated by Django 3.1.5 on 2021-02-10 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20210210_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='grid',
        ),
    ]
