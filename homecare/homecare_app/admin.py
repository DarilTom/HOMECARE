from django.contrib import admin

from .models import User
from .models import Worker
from .models import Service
from .models import Booking
from .models import Payment


admin.site.register(Worker)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Payment)