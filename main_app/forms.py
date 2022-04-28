from django.forms import ModelForm
from .models import Feeding, Profile, User

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']