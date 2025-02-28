from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from .models import Worker , Service,Booking
from .forms import SignupForm # type: ignore



def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            return redirect("login")  # Redirect to login page after signup
    else:
        form = SignupForm()
    
    return render(request, "myapp/signup.html", {"form": form})


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
    return render(request, 'myapp/landingpage.html')

def worker_profile(request, worker_id):
    worker = get_object_or_404(Worker, worker_id=worker_id)
    return render(request, 'myapp/worker_profile.html', {'worker': worker})
# Compare this snippet from homecare/homecare_app/views.py:


@login_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'myapp/servicelist.html', {'services': services})

# 25-1-25 sign up 
def signup_page(request):
    return render(request, "myapp/signup.html")


def worker_list(request, service_id):
    # Fetch the service using the service_id
    service = get_object_or_404(Service, service_id=service_id)
    # Using the related_name 'workers' to get all workers for this service
    workers = service.workers.all()
    return render(request, 'myapp/worker_list.html', {
        'service': service,
        'workers': workers,
    })
# 25-1-25 worker 
def worker_myprofile(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    return render(request, 'myapp/worker_myprofile.html', {'worker': worker})

# 28-2-25
def worker_booking_list(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    bookings = Booking.objects.filter(worker_id=worker).select_related('user_id')

    return render(request, 'myapp/worker_booking_list.html', {'worker': worker, 'bookings': bookings})