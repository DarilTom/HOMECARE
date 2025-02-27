from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# User Profile Model (Extending Django User)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    town = models.CharField(max_length=100, blank=True, null=True)
    housename = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username

# Signals to create and save UserProfile automatically
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()

# Worker Model
class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)  
    worker_name = models.CharField(max_length=100)
    worker_email = models.EmailField(max_length=100)
    worker_pass = models.CharField(max_length=100)
    worker_phone = models.CharField(max_length=15)
    worker_dob = models.DateField()
    worker_blood = models.CharField(max_length=3)
    worker_state = models.CharField(max_length=100)
    worker_district = models.CharField(max_length=100)
    worker_town = models.CharField(max_length=100)
    worker_housename = models.CharField(max_length=255)
    worker_photo = models.ImageField(upload_to='worker_photos/', null=True, blank=True)  
    servicecatagory = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='workers', null=True, blank=True)

    def __str__(self):
        return self.worker_name

# Service Model
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)  
    service_name = models.CharField(max_length=100)
    service_desc = models.TextField()
    service_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name

# Payment Model
class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    working_hour = models.IntegerField()

    def __str__(self):
        return f"Payment {self.pay_id}"

# Booking Model
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='worker_bookings')
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_bookings')
    pay_id = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='payment_bookings')
    booking_time = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.booking_id}"
