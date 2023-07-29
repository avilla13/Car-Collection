from django.contrib import admin
# import your models here
from .models import Car, Service, Feature

# Register your models here
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Feature)