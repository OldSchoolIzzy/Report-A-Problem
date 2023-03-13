from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
#view function recieves a request and sends a response, reqeust handler.

from django.contrib import messages

from .forms import CreateUserForm

def registerPage(request):
    form= CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request, 'register.html', context)
def loginPage(request):
    return render(request, 'login.html')
