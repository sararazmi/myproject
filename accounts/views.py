from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignUpForm, ProfileForm
from .models import Board


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def activity(request):
    boards = Board.objects.all()
    return render(request, 'activity.html', {'test':"tests"})
