from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm


def indexView(request):
    return render(request, 'index.html')


def registerView(request):
    if request.method == 'POST':
        regForm = RegistrationForm(request.POST)

        if regForm.is_valid():
            regForm.save()

            return redirect('users:login')
    return render(request, 'reg_page.html')


def loginView(request):
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(email=loginForm.cleaned_data['email'], password=loginForm.cleaned_data['password'])

            if user:
                login(request, user)

                return redirect('users:index')
    return render(request, 'login_page.html')
