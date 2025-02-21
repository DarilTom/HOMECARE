from django.shortcuts import render
from .models import Service

# Function to get all services
def service_list(request):
    services = Service.objects.all()  # Fetch all services from the database
    return render(request, 'service_list.html', {'services': services})
