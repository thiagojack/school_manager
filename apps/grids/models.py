from django.db import models
from django.db.models.deletion import PROTECT
from apps.subjects.models import Subject
from apps.students.models import Student

# Create your models here.

class Grid(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=PROTECT,
        blank=True,
        null=True,
    )
    subjects = models.ForeignKey(
        Subject,
        on_delete=PROTECT,
        related_name='student_subjects',
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.subjects)