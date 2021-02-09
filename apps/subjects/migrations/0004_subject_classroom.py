# Generated by Django 3.1.5 on 2021-02-09 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0004_remove_classroom_subjects'),
        ('subjects', '0003_auto_20210209_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='classroom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='classrooms.classroom'),
            preserve_default=False,
        ),
    ]
