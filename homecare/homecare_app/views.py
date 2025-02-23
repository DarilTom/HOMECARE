from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from .models import Worker

def landing_page(request):
    return render(request, 'myapp/landingpage.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'myapp/home.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def worker_profile(request, worker_id):
    worker = get_object_or_404(Worker, worker_id=worker_id)
    return render(request, 'myapp/worker_profile.html', {'worker': worker})
# Compare this snippet from homecare/homecare_app/views.py: