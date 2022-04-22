from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Dog

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dog_list = Dog.objects.all()
    context = {
        'dog_list': dog_list
    }
    return render(request, 'dogs/index.html', context)

def dogs_detail(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})
