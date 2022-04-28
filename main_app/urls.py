from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Dog
    path('dogs/', views.dogs_index, name='index'),
    path('<int:dog_id>/', views.dogs_detail, name='detail'),
    path('dogs/create/', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    # relationship paths
    path('dogs/<int:dog_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('dogs/<int:dog_id>/add_photo', views.add_photo, name='add_photo'),
    path('dogs/<int:dog_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('dogs/<int:dog_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
    # Toy
    path('toys/', views.ToyIndex.as_view(), name='toy_list'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name="toy_detail"),
    path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy_delete'),
    # User
    path('accounts/signup/', views.signup, name='signup'),
    # Profile
    path('user', views.userpage, name='userpage'),
    path('accounts/update/<int:user_id>/', views.edit_user, name='account_update')
]