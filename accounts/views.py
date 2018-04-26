from django.contrib.auth import login as authorize_login
from .forms import SignUpForm
from django.shortcuts import render, redirect
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            authorize_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render( request, 'signup.html', {'form': form})
