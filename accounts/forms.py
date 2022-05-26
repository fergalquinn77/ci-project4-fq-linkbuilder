from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile

#Form for user registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#Form to update user details
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#Form to update user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = [
            'company_name',
            'twitter',
            'instagram',
            'facebook',
            'profile_image']
