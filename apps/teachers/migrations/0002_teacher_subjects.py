# Generated by Django 3.1.5 on 2021-02-09 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20210209_1218'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(to='subjects.Subject'),
        ),
    ]