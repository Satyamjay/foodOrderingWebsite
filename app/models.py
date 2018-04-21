from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm

# ###############################################-----------------VALIDATORS----------------##################################################################


# Validator for mobile number
def validate_mobile(value):
    if not (value.isdigit()):
        raise ValidationError('%(value)s is not a valid mobile number', params={'value': value},)


# Validator for pincode
def validate_pincode(value):
    if not (value.isdigit()):
        raise ValidationError('%(value)s is not a valid Pincode', params={'value': value},)

# Validator for password





# ####################################################----------------MODELS--------------####################################################################


# Available States Model
class state(models.Model):
    state_code = models.CharField(max_length=2, primary_key=True)
    state_name = models.CharField(max_length=20)
    available = models.NullBooleanField()

    def __str__(self):
        return self.state_name


# Available Cities Model
class Cities(models.Model):
    belongs_to = models.ForeignKey(state, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name


# Customer Model
class Customer(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mobile_no = models.CharField(unique=True, validators=[validate_mobile], max_length=10)
    state = models.ForeignKey(state, on_delete=models.CASCADE, max_length=20)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, max_length=20)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.email


# Restaurant Model
class Restaurant(models.Model):

    restaurant_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mobile_no = models.CharField(unique=True, validators=[validate_mobile], max_length=10)
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, max_length=20)
    pincode = models.CharField(max_length=8, validators=[validate_pincode])
    street_address = models.CharField(max_length=100)
    password = models.CharField(max_length=256)
    unique_id = models.CharField(max_length=256)

    def __str__(self):
        return self.email



# ##########################################-----------------------MODEL FORMS---------------------------####################################################

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
        self.fields['mobile_no'].widget.attrs.update({'placeholder': 'Enter Mobile Numbers', 'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'placeholder': 'Enter City', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'type': 'password'})


# Restaurant Model Form
class RestaurantForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    unique_id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'manager_name', 'email', 'mobile_no', 'state', 'city', 'pincode', 'street_address', 'password', 'unique_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['restaurant_name'].widget.attrs.update({'placeholder': 'Enter Name', 'class': 'form-control'})
        self.fields['manager_name'].widget.attrs.update({'placeholder': 'Enter Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email', 'class': 'form-control'})
        self.fields['mobile_no'].widget.attrs.update({'placeholder': 'Enter Mobile Number   ', 'class': 'form-control'})
        self.fields['state'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'placeholder': 'Enter City', 'class': 'form-control'})
        self.fields['pincode'].widget.attrs.update({'placeholder': 'Enter City', 'class': 'form-control'})
        self.fields['street_address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Address'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'type': 'password'})