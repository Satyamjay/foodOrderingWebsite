from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm

# Validate function to validate mobile number

def validate_mobile(value):
    if not (value.isdigit()):
        raise ValidationError('%(value)s is not a valid mobile number', params={'value': value},)

def validate_pincode(value):
    if not (value.isdigit()):
        raise ValidationError('%(value)s is not a valid mobile number', params={'value': value},)


# Customer Model
class Customer(models.Model):

    # Choices for states

    STATES = (
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UT', 'Uttarakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),)

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mobile_no = models.CharField(unique=True, validators=[validate_mobile], max_length=10)
    state = models.CharField(choices=STATES, max_length=2)
    city = models.CharField(max_length=20)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.email


class Restaurant(models.Model):

    STATES = (
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CT', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OR', 'Odisha'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TG', 'Telangana'),
        ('TR', 'Tripura'),
        ('UT', 'Uttarakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LD', 'Lakshadweep'),
        ('PY', 'Puducherry'),)

    restaurant_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mobile_no = models.CharField(unique=True, validators=[validate_mobile], max_length=10)
    state = models.CharField(choices=STATES, max_length=2)
    city = models.CharField(max_length=20)
    pincode = models.CharField(max_length=8, validators=[validate_pincode])
    full_address = models.CharField(max_length=100)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.email




# Customer Model Form
class CustomerForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ['name', 'email', 'mobile_no', 'state', 'city', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email', 'class': 'form-control'})
        self.fields['mobile_no'].widget.attrs.update({'placeholder': 'Enter Mobile Number   ', 'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'placeholder': 'Enter City', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'type': 'password'})

