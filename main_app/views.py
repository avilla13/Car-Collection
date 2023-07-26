from django.shortcuts import render

cars = [
   {'make': 'Ford', 'model': 'Mustang', 'year': '1967','engine': 'V8' },
   {'make': 'Dodge', 'model': 'Charger', 'year': '1969','engine': 'V8' },
   {'make': 'Dodge', 'model': 'Challenger', 'year': '1970','engine': 'V8' },
   {'make': 'Chevrolet', 'model': 'Camaro', 'year': '1969','engine': 'V8' },
   {'make': 'Buick', 'model': 'Grand National', 'year': '1987','engine': 'V6' }
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
   return render(request, 'cars/index.html', {
      'cars': cars
   })

