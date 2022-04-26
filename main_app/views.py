from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic.edit import CreateView

from .models import Dog

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    context = {
        'dogs': dogs
    }
    return render(request, 'dogs/index.html', context)

def dogs_detail(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})

def add_dogs(request):
    return render(request, 'dogs/add.html')

def new_dog(request):
    print(request.body)
#   new = Dog.objects.create(name=, breed=, description=, age=)
#   new.save()
#   return HTTPResponseRedirect('dogs/index.html')