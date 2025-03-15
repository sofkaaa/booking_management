from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def register(request: HttpRequest):

    if request.method == "GET":
        form = UserCreationForm()
        
    elif request.method =="POST":
        form = UserCreationForm(request.POST )

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('/')

    return render(request, "registration/register.html", {'form': form})
