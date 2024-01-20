from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignUpForm, ProfileForm


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


def Profile(request):
    if request.method == 'POST':
        form = Profile(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'Profile.html', {'form': form})

