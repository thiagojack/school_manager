from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class SchoolYear(models.Model):
        
    CLASSROOM_TYPE = (
        ('primary', 'Primary'),
        ('colegial', 'Colegial'),
    )

    class YearChoice(models.TextChoices):
        def create_tuple():
            year_dict = {}
            for year in range(1, 10):
                year_dict[str(year)] = str(year)
            year_tuple = [(k, v) for k, v in year_dict.items()]
            return year_tuple


    type = models.CharField(
        max_length=10,
        choices=CLASSROOM_TYPE,
    )
    lective_year = models.CharField(
        max_length=1,
        choices=YearChoice.create_tuple(),
    )

    def __str__(self):
        return str(self.type.title() + ' ' + self.lective_year)


class Classroom(models.Model):

    SHIFTS_CHOICES = (
        ('matutinal', 'Matutinal'),
        ('vespertine', 'Vespertine'),
        ('nocturnal', 'Nocturnal'),
    )

    IDENTIFIED_CHOICES = (
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    )

    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=PROTECT,
    )
    identified = models.CharField(
        max_length=1,
        choices=IDENTIFIED_CHOICES,
    )
    description = models.TextField(max_length=200)
    
    shift = models.CharField(
        max_length=10,
        choices=SHIFTS_CHOICES,
    )

    def __str__(self):
        return self.identified.upper()