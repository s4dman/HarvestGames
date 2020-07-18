from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, UserAuthenticationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('personal:home')
        else:
            context['registration_form'] = form  # Read the errors in form
    else:  # GET request; Users will see the registration form at first
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('personal:home')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('personal:home')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('personal:home')

    else:
        form = UserAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)
