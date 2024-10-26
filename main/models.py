from django.db import models
from datetime import timedelta

# Create your models here.


class Recipes(models.Model):
    name = models.CharField(max_length=250)
    prep_time = models.DurationField(default=timedelta(minutes=120))
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2,'Regular'),
        (3,'Hard')
    ]
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES)
    is_veg = models.BooleanField(default=False)
    img = models.ImageField(upload_to='recipes/')
    description = models.TextField()