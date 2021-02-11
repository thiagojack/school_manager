from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, RESTRICT
from apps.classrooms.models import Classroom, SchoolYear

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    lactive_year = models.ForeignKey(
        SchoolYear,
        on_delete=PROTECT,
        blank=True,
        null=True,
    )
    classrooms = models.ForeignKey(
        Classroom,
        on_delete=models.PROTECT,
        blank=True,
    )

    def __str__(self):
        return self.name
