from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from app.models import Customer, CustomerForm
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




def customer_form(request):
    if request.method == 'POST':
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
            return render(request, 'index.html', {'form': cust_sign_form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()
        return render(request, 'index.html', {'form': form})


def customer_login(request):
    if request.method == 'POST':
        return HttpResponse('/thanks/')

    else:
        print >>sys.stderr, 'Goodbye, cruel world!'
        form = CustomerForm()
        return render(request, 'index.html', {'form': form})
