from django.forms import ModelForm
from .models import Feeding, Profile, User

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']