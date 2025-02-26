from django.urls import path
from .views import user_login, home, user_logout, worker_profile
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login', user_login, name='login'),
    path('home/', home, name='home'),
    path('logout/', user_logout, name='logout'),
    path('worker/<int:worker_id>/', worker_profile, name='worker_profile'),
    path('services/',views.service_list, name='service_list'),
    path('workers/<int:service_id>/', views.worker_list, name='worker_list'),
#   25-1-25
   path('worker/profile/<int:worker_id>/', views.worker_myprofile, name='worker_profile'),
]