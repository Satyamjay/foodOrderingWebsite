from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.models import Customer, CustomerForm




def customer_form(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        cust_sign_form = CustomerForm(request.POST, request.FILES)
        # check whether it's valid:
        if cust_sign_form.is_valid():
            # process the data in form.cleaned_data as required
            cust_sign_form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        else:
            return render(request, 'index.html', {'form': cust_sign_form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()
        return render(request, 'index.html', {'form': form})