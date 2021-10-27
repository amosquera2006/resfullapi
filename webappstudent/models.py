from django.db import models

# Create your models here.

class emplStud(models.Model):

    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    grade = models.IntegerField()

    def __str__(self):
        return self.firstname


