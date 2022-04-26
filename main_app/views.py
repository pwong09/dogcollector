from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from .forms import FeedingForm
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
    feeding_form = FeedingForm()
    available_toys = Toy.objects.exclude(id__in = dog.toys.all().values_list('id'))
    return render(request, 'dogs/detail.html', {
        'dog': dog,
        'feeding_form': feeding_form,
        'toys': available_toys
        })

def add_feeding(request, dog_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)

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

def assoc_toy(request, dog_id, toy_id):
    Dog.objects.get(id=dog_id).toys.add(toy_id)
    return redirect('detail', dog_id=dog_id)