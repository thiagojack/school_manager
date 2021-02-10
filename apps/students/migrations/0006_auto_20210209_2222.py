# Generated by Django 3.1.5 on 2021-02-09 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0007_subject_teacher'),
        ('classrooms', '0011_remove_classroom_subjects'),
        ('students', '0005_student_lactive_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classrooms',
            field=models.ManyToManyField(blank=True, to='classrooms.Classroom'),
        ),
        migrations.CreateModel(
            name='Grid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
            ],
        ),
    ]