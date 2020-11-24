from django.db import models
from django.conf import settings

# Create your models here.
class Miles(models.Model):
    miles_on_car = models.CharField(max_length=100)
    def __str__(self):
        return self.miles_on_car

class Fuel(models.Model):
    car_fuel = models.CharField(max_length=10)
    def __str__(self):
        return self.car_fuel

class Body(models.Model):
    car_body = models.CharField(max_length=100)
    def __str__(self):
        return self.car_body

class Transmission(models.Model):
    car_transmission = models.CharField(max_length=20)
    def __str__(self):
        return self.car_transmission

class Features(models.Model):
    car_features = models.CharField(max_length=100)
    def __str__(self):
        return self.car_features

class CarDetails(models.Model):
    owner_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=13)
    price = models.IntegerField()
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=30)
    production_year = models.IntegerField(null=True,blank=True)
    car_miles = models.ForeignKey(Miles,on_delete=models.CASCADE,related_name='total_car_miles')
    fuel_type = models.ForeignKey(Fuel,on_delete=models.CASCADE, related_name='car_fuel_type')
    seating_capacity = models.IntegerField(null=True,blank=True)
    body_type = models.ForeignKey(Body,on_delete=models.CASCADE, related_name='car_body_type')
    transmission_type = models.ForeignKey(Transmission,on_delete=models.CASCADE, related_name='car_transmission_type')
    engine_displacement = models.CharField(max_length=20)
    key_features = models.ManyToManyField(Features,related_name='car_services')
    car_image = models.ImageField(upload_to='car_image')
    car_color = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.car_model
