from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .forms import ServiceForm
# cars list was only used for initial app set up
# cars = [
#    {'make': 'Ford', 'model': 'Mustang', 'year': '1967','engine': 'V8' }
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
   # Instantiate ServiceForm to be rendered in the template
   service_form = ServiceForm()
   return render(request, 'cars/detail.html', {
      # Include the car and service_form in the context
      'car': car,
      'service_form': service_form
    })

class CarCreate(CreateView):
   model = Car
   fields = '__all__'

class CarUpdate(UpdateView):
   model = Car
   fields = '__all__'

class CarDelete(DeleteView):
   model = Car
   # Need to overwrite the redirect path like this:
   success_url = '/cars'

def add_service(request, car_id):
  # create a ModelForm instance using the data in request.POST
  form = ServiceForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the car_id assigned
    new_service = form.save(commit=False)
    new_service.car_id = car_id
    new_service.save()
  return redirect('detail', car_id=car_id)