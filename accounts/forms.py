from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Support_Tickets, Tickets_Messages


# Form for user registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Form to update user details
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Form to update user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'company_name',
            'twitter',
            'instagram',
            'facebook',
            'profile_image']

# Form for Support Tickets
class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = Support_Tickets
        fields = ['title', 'query', 'query_image']
