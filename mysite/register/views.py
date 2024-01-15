from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def change(response):
    if response.method == "POST":
        form = PasswordChangeForm(response.user, response.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(response, user)
            messages.success(response, 'Password changed sucesfully')
            return redirect("/")
        else:
            return HttpResponse("<h2>Invalid details</h2>")
    else:
        form = PasswordChangeForm(response.user)
    return render(response, "reset/change.html", {"form": form})
