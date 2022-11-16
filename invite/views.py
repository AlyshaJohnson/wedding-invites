from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def get_sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {User.first_name, User.last_name}.")  # noqa
                return redirect("/invite/")
            else:
                messages.error(request, "Invalid email or password.")
    form = AuthenticationForm()
    return render(request=request, template_name='invite/index.html', context={"login_form": form})  # noqa


def get_invite(request):
    return render(request, 'invite/invite.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/invite/")
        messages.error(request, "Unsuccessful registration. Invalid information.")  # noqa
    form = NewUserForm()
    return render(request=request, template_name="invite/register.html", context={"register_form": form})  # noqa
