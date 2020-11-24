from django import forms
from django.contrib.auth.forms import UserCreationForm
from cars.models import CarDetails
from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarDetails
        fields = ['email','phone_number','price','car_brand','car_model','production_year','car_miles','fuel_type','seating_capacity','body_type','transmission_type','engine_displacement','car_image','car_color','description','key_features']
