from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404
from .models import Worker , Service,Booking
from .forms import SignupForm # type: ignore
from django.contrib.auth.models import User
from django.contrib import messages



def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm-password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, "signup.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return render(request, "signup.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        return redirect("login")  # Redirect to login page

    return render(request, "myapp/signup.html")


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