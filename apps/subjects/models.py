from django.db import models
from django.db.models.deletion import PROTECT
from apps.classrooms.models import SchoolYear
from apps.teachers.models import Teacher

# Create your models here.

class Subject(models.Model):

    SUBJECT_CATEGORY = (
        ('exater', 'Exater'),
        ('humans', 'Humans'),
        ('biological', 'Biological'),
    )

    SUBJECT_SITUATION = (
        ('confirmed', 'Confirmed'),
        ('not confirmed', 'NOT confirmed'),
    )

    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    situation = models.CharField(
        max_length=13,
        choices=SUBJECT_SITUATION,
    )
    category = models.CharField(
        max_length=10,
        choices=SUBJECT_CATEGORY,
    )
    description = models.TextField(max_length=250)
    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=PROTECT,
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=PROTECT,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name