from django.contrib import admin

from .models import User
from .models import Worker
from .models import Service

admin.site.register(User)
admin.site.register(Worker)
admin.site.register(Service)
