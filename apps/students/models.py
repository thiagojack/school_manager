from django.db import models
from django.db.models.deletion import PROTECT
from apps.classrooms.models import Classroom, SchoolYear
from apps.subjects.models import Subject

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    lactive_year = models.ForeignKey(
        SchoolYear,
        on_delete=PROTECT,
        blank=True,
        null=True,
    )
    classrooms = models.ManyToManyField(
        Classroom,
        blank=True,
    )
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name