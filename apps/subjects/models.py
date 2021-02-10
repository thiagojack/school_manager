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

    name = models.CharField(max_length=20)
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