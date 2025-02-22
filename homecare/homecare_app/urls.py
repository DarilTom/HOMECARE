from django.urls import path
from .views import user_login, home, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', user_login, name='login'),
    path('home/', home, name='home'),
    path('logout/', user_logout, name='logout'),
]
