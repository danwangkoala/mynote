from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib import messages



def registration(response):
    if response.method == "POST":
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            
            username = response.POST['username']
            password = response.POST['password1']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                login(response, user)
                return redirect("/index")
    else:
        form = RegistrationForm()
    return render(response, "registration/registration.html", {"form":form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })