# Generated by Django 3.1.5 on 2021-02-10 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20210210_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]