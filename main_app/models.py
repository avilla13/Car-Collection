from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=75)
    year = models.IntegerField()
    engine = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.model}, id: {self.id}'