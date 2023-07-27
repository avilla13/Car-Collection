from django.shortcuts import render

from .models import Car

# cars list was only used for initial app set up
# cars = [
#    {'make': 'Ford', 'model': 'Mustang', 'year': '1967','engine': 'V8' },
#    {'make': 'Dodge', 'model': 'Charger', 'year': '1969','engine': 'V8' },
#    {'make': 'Dodge', 'model': 'Challenger', 'year': '1970','engine': 'V8' },
#    {'make': 'Chevrolet', 'model': 'Camaro', 'year': '1969','engine': 'V8' },
#    {'make': 'Buick', 'model': 'Grand National', 'year': '1987','engine': 'V6' }
# ]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
   cars = Car.objects.all()
   return render(request, 'cars/index.html', {
      'cars': cars
   })

def cars_detail(request, car_id):
   car = Car.objects.get(id=car_id)
   return render(request, 'cars/detail.html', {'car': car})


