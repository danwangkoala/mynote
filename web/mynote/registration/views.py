from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registration(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/index")
    else:
        form = RegistrationForm()
    return render(response, "registration/registration.html", {"form":form})