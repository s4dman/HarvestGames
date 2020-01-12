from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import RegistrationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form  # Read the errors in form
    else:  # GET request; Users will see the registration form at first
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)
