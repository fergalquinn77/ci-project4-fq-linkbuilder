from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import profile

# Create your views here.

def register(request):
    form=UserCreationForm()
    return render(request, 'register.html', {'form':form})

@login_required
def profile(request):
    model = profile
    return render(request, 'profile.html')

