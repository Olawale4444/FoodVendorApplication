from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Home_view(request, *args, **kwargs):
	return render ( request, "home.html", {}) 


def Register_view(request, *args, **kwargs):
	return render ( request, "register.html", {}) 


def Login_view(request, *args, **kwargs):
	return render ( request, "login.html", {}) 

def CreateMenuItem(request, *args, **kwargs):
	return render ( request, "Createmenu.html", {}) 


def Customer_view (request, *args, **kwargs):
	return render ( request, "customer.html", {}) 

