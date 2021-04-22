from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from .models import *

#landlord views

def landlord_home(request):
    return render(request, 'nyumba/landlord/landlord_home.html')

def properties(request):
    return render(request, 'nyumba/landlord/properties.html')

def individual_property(request):
    return render(request, 'nyumba/landlord/individual_property.html')

def add_property_form(request):
    return render(request, 'nyumba/landlord/add_property.html')


#tenant views
def tenant_home(request):
    return render(request, 'nyumba/tenant/tenant_home.html')


#common views
@login_required()
def logout_user(request):
	logout(request)
	return redirect('User_account:login')


