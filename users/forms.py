from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1')

class ProfileForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ('username', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'bio')


        