from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/add', views.add_dogs, name='add'),
    path('<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/new', views.new_dog, name='new')
]