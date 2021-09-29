from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from users.forms import UserLoginForm, UserRegisterForm


# Create your views here.


def login(request):
    error_data = ''
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GS: Авторизация',
        'form': form,
        'error_data': error_data
    }
    return render(request, 'users/login.html', context)


def register(request):
    errors = ''
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            errors = form.errors
    else:
        form = UserRegisterForm(data=request.POST)
    context = {
        'title': 'GS: Регистрация',
        'form': form,
        'error_data':  errors,
    }
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
