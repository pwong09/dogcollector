from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from .models import Dog, Toy

class DogCreate(CreateView):
    model = Dog
    fields = '__all__'

class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'

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
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})

class ToyIndex(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['color', 'status']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'