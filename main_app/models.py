from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=75)
    year = models.IntegerField()
    engine = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.model}, id: {self.id}'
    # to redirect after create & update functionality
    # reverse() --> url template tag that returns correct path for
    # the 'detail' named route
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
    