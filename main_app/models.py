from django.db import models
# Import the reverse function
from django.urls import reverse


SERVICES = (
    ('O', "Oil & Filter"),
    ('T', "Rotate Tires"),
    ('B', "Brake(s) Replacement"),
)

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

class Service(models.Model):
    date = models.DateField()
    service = models.CharField(max_length=1, choices=SERVICES, default=SERVICES[0][0])
    description = models.TextField(max_length=250)
    # car_id FK:
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # Override __str__ method for 'human-friendly' output
    def __str__(self):
        return f"Service record of {self.get_service_display()} on {self.date}"
    
    # Change the default date sorting
    class Meta:
        ordering = ['-date']