from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def no_of_people(self):
        return self.people
