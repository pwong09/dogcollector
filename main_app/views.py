import boto3
import uuid

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView

from .forms import FeedingForm
from .models import Dog, Toy, Photo

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'pwcollection'


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

def remove_toy(request, dog_id, toy_id):
    dog = Dog.objects.get(id=dog_id)
    toy = Toy.objects.get(id=toy_id)
    toy.dog_set.remove(dog)
    dog.toys.remove(toy)
    return redirect('detail', dog_id=dog_id)

def add_photo(request, dog_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, dog_id=dog_id)
        except:
            print('An error occured when uploading your file to S3')
    return redirect('detail', dog_id=dog_id)