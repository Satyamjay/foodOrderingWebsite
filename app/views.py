from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from app.models import CustomerForm, RestaurantForm
import pyrebase
import sys

# Get an instance of a logger
config = {
    "apiKey": "AIzaSyAwXggcEjMEkDKqHHKiQ4FK8oots1XGr_c",
    "authDomain": "foodorder-94c40.firebaseapp.com",
    "databaseURL": "https://foodorder-94c40.firebaseio.com",
    "projectId": "foodorder-94c40",
    "storageBucket": "foodorder-94c40.appspot.com",
    "messagingSenderId": "519649470924"
}

my_firebase = pyrebase.initialize_app(config)
auth = my_firebase.auth()




def signup_page(request):
    if (request.method == 'POST') and ('customer_signup' in request.POST):
        # create a form instance and populate it with data from the request:
        cust_sign_form = CustomerForm(request.POST, request.FILES)
        # check whether it's valid:
        if cust_sign_form.is_valid():
            # process the data in form.cleaned_data as required
            cust_sign_form.save()
            #Adding User to Firebase
            user = auth.create_user_with_email_and_password(cust_sign_form.cleaned_data['email'], cust_sign_form.cleaned_data['password'])
            auth.send_email_verification(user['idToken'])
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        else:
            form2 = RestaurantForm()
            return render(request, 'signup.html', {'form': cust_sign_form, 'form2': form2})

    elif (request.method == 'POST') and ('restaurant_signup' in request.POST):
        # create a form instance and populate it with data from the request:
        restaurant_signup_form = RestaurantForm(request.POST, request.FILES)
        # check whether it's valid:
        if restaurant_signup_form.is_valid():
            # process the data in form.cleaned_data as required
            restaurant_signup_form.save()
            # Adding User to Firebase
            user = auth.create_user_with_email_and_password(restaurant_signup_form.cleaned_data['email'], restaurant_signup_form.cleaned_data['password'])
            auth.send_email_verification(user['idToken'])
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks2/')
        else:
            form = CustomerForm()
            return render(request, 'signup.html', {'form': form, 'form2': restaurant_signup_form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()
        form2 = RestaurantForm()
        return render(request, 'signup.html', {'form': form, 'form2': form2})



def login_page(request):
    return render(request, 'login.html', {})