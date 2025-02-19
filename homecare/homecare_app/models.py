from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)  
#     user_name = models.CharField(max_length=100)
#     user_email = models.EmailField(max_length=100)
#     user_pass = models.CharField(max_length=100)
#     user_blood = models.CharField(max_length=3)
#     user_phone = models.CharField(max_length=15)
#     user_address = models.TextField()

#     def __str__(self):
#         return self.user_name


class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)  
    worker_name = models.CharField(max_length=100)
    worker_email = models.EmailField(max_length=100)
    worker_pass = models.CharField(max_length=100)
    worker_phone = models.CharField(max_length=15)
    worker_dob = models.DateField()
    worker_blood = models.CharField(max_length=3)
    worker_address = models.TextField()

    def __str__(self):
        return self.worker_name


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)  
    service_name = models.CharField(max_length=100)
    service_desc = models.TextField()
    service_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name
    


class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    working_hour = models.IntegerField()

    def __str__(self):
        return f"Payment {self.pay_id}"




class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    pay_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    booking_time = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.booking_id}"



