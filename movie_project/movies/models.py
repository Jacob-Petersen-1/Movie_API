from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=8,decimal_places=2)